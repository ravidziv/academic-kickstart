#!/usr/bin/env python3
"""Check built Hugo output without third-party dependencies.

Usage: python3 scripts/check_site.py public [--baseline ../baseline-public]
"""
import argparse
from collections import defaultdict
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.meta = defaultdict(list)
        self.links = []
        self.assets = []
        self.ids = set()
        self.h1 = []
        self.schemas = []
        self.sections = defaultdict(list)
        self.section_text = defaultdict(str)
        self.profile_links = []
        self.hidden_profile_links = False
        self.canonical = []
        self.title = ''
        self.text = ''
        self._heading = None
        self._title = False
        self._schema = None
        self._section_stack = []
        self._profile = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'section':
            self._section_stack.append(a.get('id', ''))
        if tag == 'title':
            self._title = True
        if tag == 'h1':
            self._heading = ''
        if tag == 'meta':
            self.meta[a.get('name') or a.get('property')].append(a.get('content', ''))
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical.append(a.get('href'))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self._schema = ''
        if tag == 'ul' and 'network-icon' in a.get('class', '').split():
            self.hidden_profile_links = self.hidden_profile_links or a.get('aria-hidden') == 'true'
            self._profile = True
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
            if self._section_stack:
                self.sections[self._section_stack[-1]].append(a['href'])
            if self._profile:
                self.profile_links.append(a)
        if tag in ('img', 'script') and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet':
            self.assets.append(a.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'title':
            self._title = False
        if tag == 'h1' and self._heading is not None:
            self.h1.append(self._heading.strip())
            self._heading = None
        if tag == 'script' and self._schema is not None:
            self.schemas.append(json.loads(self._schema))
            self._schema = None
        if tag == 'section' and self._section_stack:
            self._section_stack.pop()
        if tag == 'ul':
            self._profile = False

    def handle_data(self, data):
        self.text += data
        if self._section_stack:
            self.section_text[self._section_stack[-1]] += data
        if self._title:
            self.title += data
        if self._heading is not None:
            self._heading += data
        if self._schema is not None:
            self._schema += data


def schema_nodes(items):
    for item in items:
        if isinstance(item, dict):
            yield item
            yield from schema_nodes(item.values())
        elif isinstance(item, list):
            yield from schema_nodes(item)


def target_file(root, current, href):
    local_url = '/' + str(current.relative_to(root))
    resolved = urlsplit(urljoin('https://www.ravid-shwartz-ziv.com' + local_url, href))
    if resolved.scheme not in ('http', 'https') or resolved.netloc != 'www.ravid-shwartz-ziv.com':
        return None
    path = root / unquote(resolved.path).lstrip('/')
    if resolved.path.endswith('/') or path.is_dir():
        path /= 'index.html'
    return path


def missing_targets(root, pages):
    missing = set()
    for page in pages:
        for href in page.links + page.assets:
            if not href or href.startswith('#'):
                continue
            target = target_file(root, page.path, href)
            if target is not None and not target.exists():
                missing.add((str(page.path.relative_to(root)), href))
    return missing


def content_pages(root):
    # Bundled reveal.js contains its own unlinked demo/utility HTML. Validate
    # generated site pages, not the internals of that unchanged vendor library.
    return [Page(p) for p in root.rglob('*.html') if p.relative_to(root).parts[0] != 'js']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    parser.add_argument('--baseline', type=Path)
    args = parser.parse_args()
    root = args.output.resolve()
    pages = content_pages(root)
    home = next(p for p in pages if p.path == root / 'index.html')
    assert home.h1 == ['Ravid Shwartz Ziv'], home.h1
    assert home.title == 'Ravid Shwartz Ziv | AI Research'
    assert home.canonical == ['https://www.ravid-shwartz-ziv.com/']
    assert len(home.meta['description']) == 1 and home.meta['description'][0].strip()
    assert home.meta['og:description'] == home.meta['description']
    assert home.meta['twitter:creator'] == ['@ziv_ravid']
    assert home.meta['twitter:card'] == ['summary_large_image']
    assert len(home.meta['og:image']) == 1
    assert 'logo' not in home.meta['og:image'][0]
    assert target_file(root, home.path, home.meta['og:image'][0]).is_file()
    assert home.meta['og:image:alt'][0].strip()
    assert {'about', 'focus', 'experience', 'featured', 'publications', 'contact', 'work', 'podcast'} <= home.ids
    assert 'talks' not in home.ids
    assert all(a.get('aria-label', '').strip() for a in home.profile_links)
    assert not home.hidden_profile_links
    assert len(home.profile_links) == 6
    for href in home.links:
        if href.startswith('#') and len(href) > 1:
            assert unquote(href[1:]) in home.ids, 'Missing homepage anchor: ' + href

    nodes = list(schema_nodes(home.schemas))
    people = [n for n in nodes if n.get('@type') == 'Person']
    assert len(people) == 1
    person = people[0]
    assert person['name'] == 'Ravid Shwartz Ziv'
    assert person['alternateName'] == ['Ravid Shwartz-Ziv']
    assert person['@id'] == home.canonical[0] + '#person'
    assert person['url'] == home.canonical[0]
    assert person['jobTitle'] == 'AI Researcher'
    assert person['worksFor'][0]['name'] == 'Meta Superintelligence Labs (MSL)'
    assert person['knowsAbout'][:3] == ['World Models', 'Memory & Personalization', 'Model Compression']
    assert target_file(root, home.path, person['image']).is_file()
    assert set(person['sameAs']) <= set(home.links)
    assert not any('bottleneck' in u or 'ai.meta.com' in u for u in person['sameAs'])
    profile = next(n for n in nodes if n.get('@type') == 'ProfilePage')
    assert profile['mainEntity']['@id'] == person['@id']

    def publications(section):
        return list(dict.fromkeys(u for u in home.sections[section]
                                  if '/publication/' in u and urlsplit(u).path != '/publication/'))
    featured = publications('featured')
    recent = publications('publications')
    assert len(featured) == 6, featured
    assert len(recent) == 3, recent
    assert not set(featured) & set(recent)
    assert [urlsplit(u).path for u in featured[:2]] == ['/publication/layer-by-layer/', '/publication/minp/']
    assert {urlsplit(u).path for u in featured[2:]} == {
        '/publication/s-jepa/', '/publication/training-in-imagination/',
        '/publication/task-aware-quantization/', '/publication/attention-sinks-compression-valleys/',
    }
    assert [urlsplit(u).path for u in recent] == [
        '/publication/dry-sampling/', '/publication/xtc-sampling/', '/publication/hp-jepa/',
    ]
    assert 'Former appointment · started September 2021' in home.text
    assert 'August 2025 – Present' in home.section_text['experience']
    assert 'January 2023 – August 2025' in home.section_text['experience']
    assert 'Started January 2023' not in home.section_text['experience']
    assert 'Research into practice' in home.text
    assert 'Hebrew University of Jerusalem' in home.text
    about = home.section_text['about']
    for surface in (about, person['description']):
        assert 'information theory and computational neuroscience' in surface
    assert 'world models, memory, and compression' in about.lower()
    assert 'continual learning' in about.lower()
    assert 'Previously, I was an Assistant Professor and Faculty Fellow at NYU' in about
    assert 'Center for Data Science' in about
    assert 'Former Assistant Professor and Faculty Fellow at NYU' in person['description']
    assert home.meta['description'][0] == 'Ravid Shwartz Ziv is an AI researcher at Meta MSL working on world models, memory, model compression, and continual learning; formerly faculty at NYU.'
    assert 'Ph.D. with Tali Tishby' in about
    assert 'postdoctoral research with Yann LeCun' in about
    assert 'postdoctoral research with Yann LeCun. My background is in information theory and computational neuroscience' in about
    assert 'My industry experience spans Wand AI, Intel, Google AI, and Wikipedia.' in about
    assert 'My industry experience spans Wand AI, Intel, Google AI, and Wikipedia.' in person['description']
    assert 'Share an idea' in about
    assert 'AI research writing & podcast:' in about
    assert home.sections['about'].count('https://www.the-information-bottleneck.com/') >= 2
    assert 'I write about AI research' not in about
    assert 'co-host the podcast with Allen Roush' not in about
    assert 'I write about AI research' in home.section_text['podcast']
    assert 'co-host the podcast with Allen Roush' in home.section_text['podcast']
    assert 'Essays and podcast conversations about the ideas and engineering behind AI' in home.section_text['podcast']
    assert 'the assumptions, tradeoffs, and engineering decisions' in home.section_text['podcast']
    assert 'compressing information while preserving what matters for a task' in home.section_text['podcast']
    assert 'Selected writing' in home.section_text['podcast']
    assert 'Writing & Podcast' in home.text
    for slug in ('editing-a-compressed-memory', 'speculative-decoding-from-zero-to'):
        assert 'https://www.the-information-bottleneck.com/p/' + slug in home.sections['podcast']
    assert 'https://www.the-information-bottleneck.com/archive' in home.sections['podcast']
    assert 'interesting ideas and explore new collaborations' in home.section_text['contact']
    assert 'mailto:ravidziv@gmail.com' in home.sections['contact']
    assert 'Research collaborations' in home.section_text['work']
    assert 'joint research projects' in home.section_text['work']
    assert 'a joint project in mind' in home.section_text['contact']
    assert 'Advising startups and companies' not in home.text
    assert 'advisor to startups and companies' not in person['description']
    assert 'advisor to startups and companies' not in home.meta['description'][0]
    assert '#contact' in home.sections['work']
    assert '/publication/s-jepa/' in home.sections['work']
    assert 'https://github.com/gioannides/s-jepa' in home.sections['work']
    assert 'World models & JEPA' in home.section_text['work']
    assert 'Learning speech representations' in home.section_text['work']
    assert 'From information theory to working AI systems.' not in home.text
    assert 'Meta FAIR' not in home.text
    assert 'Three connected directions' in home.section_text['focus']
    assert 'Understand & predict' in home.section_text['focus']
    assert 'Retain & adapt' in home.section_text['focus']
    assert 'Build efficiently' in home.section_text['focus']
    assert home.sections['focus'] == [
        '/research/world-models/', '/research/memory-continual-learning/',
        '/research/model-compression-efficient-ai/',
    ]
    assert 'Earlier industry and research roles' in home.section_text['experience']
    assert '/talk/' in home.sections['experience']
    assert '#talks' not in home.links
    for slug, title, phrase in [
        ('world-models', 'World Models and Predictive Representations', 'On Training in Imagination'),
        ('memory-continual-learning', 'Memory, Personalization, and Continual Learning', 'Editing a Compressed Memory'),
        ('model-compression-efficient-ai', 'Model Compression and Efficient AI', 'You Had One Job'),
    ]:
        page = next(p for p in pages if p.path == root / 'research' / slug / 'index.html')
        assert page.h1 == [title], slug
        assert page.canonical == ['https://www.ravid-shwartz-ziv.com/research/' + slug + '/'], slug
        assert len(page.meta['description']) == 1 and page.meta['description'][0].strip(), slug
        assert phrase in page.text, slug
        assert 'Jan 1, 0001' not in page.text, slug
    robots = (root / 'robots.txt').read_text()
    assert 'User-agent: *' in robots and 'Allow: /' in robots
    assert 'Sitemap: https://www.ravid-shwartz-ziv.com/sitemap.xml' in robots
    for slug in ('layer-by-layer', 'minp', 'minitap', 'situational-judgment-tests', 'chess-conceptual-alignment', 'thinking-beyond-tokens', 'inuit', 's-jepa', 'jepa-neural-tokenizer', 'hp-jepa'):
        page = next(p for p in pages if p.path == root / 'publication' / slug / 'index.html')
        assert len(page.h1) == 1, slug
        assert (page.path.parent / 'cite.bib').is_file(), slug
        assert any('arxiv.org' in u for u in page.links), slug
    for slug, arxiv_id in {'s-jepa': '2606.19398', 'jepa-neural-tokenizer': '2512.07168', 'hp-jepa': '2608.00491'}.items():
        page = next(p for p in pages if p.path == root / 'publication' / slug / 'index.html')
        assert 'https://arxiv.org/abs/' + arxiv_id in page.links, slug
        assert 'Ravid Shwartz Ziv' in page.text, slug
    audited = {
        'dry-sampling': '2608.22761', 'xtc-sampling': '2608.22758',
        'mirage-probes': '2606.13870', 'training-in-imagination': '2605.06732',
        'latent-transfer-attack': '2603.06311', 'superhuman-adaptable-intelligence': '2602.23643',
        'uat-lite': '2602.02952', 'beyond-the-loss-curve': '2602.00315',
        'gmm-anchored-jepa': '2602.09040', 'ai-expertise-under-uncertainty': '2601.05500',
        'deepdebater': '2511.17854', 'task-aware-quantization': '2511.06516',
        'antislop': '2510.15061', 'attention-sinks-compression-valleys': '2510.06477',
        'illusion-of-progress': '2508.08285', 'layer-importance-math-reasoning': '2506.22638',
        'tokens-to-thoughts': '2505.17117', 'ndlinear': '2503.17353', 'rate-in': '2412.07169',
        'uncertainty-aware-priors': None,
    }
    for slug, arxiv_id in audited.items():
        page = next(p for p in pages if p.path == root / 'publication' / slug / 'index.html')
        assert len(page.h1) == 1 and 'Ravid Shwartz Ziv' in page.text, slug
        assert page.canonical == ['https://www.ravid-shwartz-ziv.com/publication/' + slug + '/'], slug
        citation = (page.path.parent / 'cite.bib').read_text()
        assert 'Ravid Shwartz-Ziv' in citation, slug
        if arxiv_id:
            assert 'https://arxiv.org/abs/' + arxiv_id in page.links, slug
            assert 'eprint={' + arxiv_id + '}' in citation, slug
        else:
            assert 'https://proceedings.mlr.press/v258/rudner25a.html' in page.links, slug
    for slug, label in {
        'layer-by-layer': 'ICML 2025 (Oral)',
        'task-aware-quantization': 'ICML 2026 AdaptFM Workshop',
        'mirage-probes': 'ICML 2026 EMM-QA Workshop (Spotlight)',
        'tokens-to-thoughts': 'ICLR 2026',
        'attention-sinks-compression-valleys': 'ICLR 2026',
        'antislop': 'ICLR 2026',
        'layer-importance-math-reasoning': 'NeurIPS 2025 MATH-AI Workshop',
        'chess-conceptual-alignment': 'NeurIPS 2025 Creative AI Track',
    }.items():
        assert label in home.text or label in next(p.text for p in pages if p.path == root / 'publication' / slug / 'index.html'), slug
    livebench = next(p for p in pages if p.path == root / 'publication/livebanch/index.html')
    assert 'Contamination-Limited' in livebench.h1[0]
    assert 'Contamination-Free' not in livebench.h1[0]
    for page in pages:
        assert 'github.com/example/inheritune' not in page.text
        assert not any('Ravid99216606' in u for u in page.links)
    sitemap = ET.parse(root / 'sitemap.xml')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    home_node = next(n for n in sitemap.findall('s:url', ns) if n.findtext('s:loc', namespaces=ns) == home.canonical[0])
    lastmod = home_node.findtext('s:lastmod', namespaces=ns)
    assert lastmod[:10] == profile['dateModified'][:10] == home.meta['og:updated_time'][0][:10]

    broken = missing_targets(root, pages)
    known = set()
    if args.baseline:
        baseline = args.baseline.resolve()
        old_pages = content_pages(baseline)
        known = missing_targets(baseline, old_pages)
        # Publication and talk page URLs must remain available; taxonomy pagination
        # and hashed resource URLs may legitimately change.
        for section in ('publication', 'talk'):
            for old in (baseline / section).glob('*/index.html'):
                if old.parent.name != 'page':
                    assert (root / old.relative_to(baseline)).exists(), old
    regressions = broken - known
    assert not regressions, 'New broken internal links: ' + repr(sorted(regressions)[:20])
    print(f'PASS: {len(pages)} HTML pages; homepage SEO, identity schema, headings, publication selection, assets, citations, preserved URLs, and internal links.')
    if broken:
        print(f'{len(broken)} pre-existing broken internal link references remain outside this update.')


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, StopIteration, ValueError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
