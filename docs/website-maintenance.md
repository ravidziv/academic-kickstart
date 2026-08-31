# Website maintenance

The site remains on Hugo Academic 4.8 and the existing Netlify configuration,
using Hugo **0.72.0 Extended**. Theme changes live in project-level `layouts/`
overrides and `assets/scss/custom.scss`; the theme submodule is unchanged.

## Content

- Profile and affiliations: `content/authors/admin/_index.md`.
- Applied work: `content/home/work.md`.
- S-JEPA leads the applied-work cards under World models & JEPA. Its description
  identifies the actual task as speech representation learning; it is not
  described as a complete world simulator.
- The collaboration block is the Markdown body of `content/home/work.md`.
  It includes joint research projects and informal guidance across academia
  and industry, without presenting a separate commercial advisory service.
- Writing and podcast: `content/home/podcast.md`. Keep the `#podcast` anchor
  stable. The section links directly to authored essays as well as listening
  platforms, and the navigation label is Writing & Podcast. A restrained text
  link in the hero gives The Information Bottleneck visibility without adding
  another biography paragraph.
- Research overview: `content/home/focus.md` and the `research_focus` widget.
  Its three cards link to the evergreen topic pages under `content/research/`:
  world models, memory and continual learning, and model compression. Keep
  these routes stable because they are the main topical search landing pages.
- Experience: `content/home/experience.md`. Use `date_label` when exact dates
  are unavailable; only confirmed current roles should have `current = true`.
  Current and most relevant appointments use `secondary = false`; earlier
  roles use `secondary = true` and render inside a collapsed details element.
- Talks no longer occupy a long homepage section. `content/home/talks.md`
  remains inactive, while `/talk/` and every existing talk URL remain public
  and linked from Experience.
- Publications: each `content/publication/<slug>/` folder contains the page
  and its `cite.bib`. Preserve existing slugs when updating a paper.
- Selected research: six papers have `featured: true`. Recent Publications
  excludes these so entries are not repeated.
- `content.pinned` in `content/home/featured.md` puts Layer by Layer and Min-p
  first without changing their dates. The remaining selected papers follow in
  descending date order. Every pinned page must exist and be featured.
- The current six selections are Layer by Layer, Min-p, S-JEPA, On Training in
  Imagination, You Had One Job (Task-Aware Quantization), and Attention Sinks
  and Compression Valleys. Inheritune and Minitap remain in applied work;
  the other JEPA papers and From Tokens to Thoughts remain in the archive.
- Project overrides for `li_compact.html` and `page_metadata.html` show
  `publication_short` in lists and detail pages. This makes workshop/preprint
  status and conference years visible independently of original release dates.

The homepage presents research alongside practical methods, benchmarks, and
systems. Project descriptions refer to collaborative work; they do not assert
undocumented product deployments or sole ownership.

The profile's `interests` list drives structured research metadata. The hero
shows the three leading themes—world models, memory, and compression—while
continual learning remains explicit in the biography, focus map, topic page,
and structured data. The user confirmed the current
affiliation as Meta Superintelligence Labs (MSL), the former Assistant Professor
and Faculty Fellow appointment at NYU, Ph.D. supervision by Tali Tishby, postdoctoral research with
Yann LeCun, and collaborative research and guidance across academia and industry.

`identity: true` on a social profile includes it in `Person.sameAs`. Do not use
this flag for an employer's general website or a podcast's homepage.

Update `lastmod` in `content/_index.md` when the homepage changes meaningfully.
Preserve actual publication dates; do not refresh them to make papers look new.
The homepage search title is `Ravid Shwartz Ziv | AI Research`; keep employer
details in the page copy and structured profile rather than the title tag.
The preferred display name has no hyphen. Keep `Ravid Shwartz-Ziv` in
`alternate_names` and in publication metadata where that spelling is part of
the published citation.
`enableRobotsTXT` and `layouts/robots.txt` expose the sitemap to crawlers. The
static checker validates the three topic pages, their canonical URLs, unique
descriptions, `robots.txt`, and preservation of the talk/publication archives.

## Checks

```sh
hugo --gc --minify --environment production --baseURL https://www.ravid-shwartz-ziv.com/
python3 scripts/check_site.py public
```

For a larger edit, build the previous version into a separate directory and
pass `--baseline <directory>` to check that publication/talk URLs remain intact.
The checker validates generated content pages, not demo HTML bundled inside
the unchanged reveal.js vendor assets.

## Sources for the August 2026 update

The expanded [recent-publication audit](recent-publications-2026.md) records
20 additional entries, their verified sources, and the selection rationale.
It compares arXiv records under both hyphenated and unhyphenated name variants
with official conference records. Treat it as a dated metadata/content audit,
not an automatically updating or exhaustive bibliography.

- [Layer by Layer, ICML 2025](https://proceedings.mlr.press/v267/skean25a.html)
- [Min-p, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/afa5f124e36bed5cc2125067005d43f5-Abstract-Conference.html)
- [Min-p authors, first release, revisions, and oral status](https://arxiv.org/abs/2407.01082)
- [S-JEPA](https://arxiv.org/abs/2606.19398)
- [JEPA as a Neural Tokenizer, NeurIPS 2025 UniReps Workshop](https://arxiv.org/abs/2512.07168)
- [HP-JEPA](https://arxiv.org/abs/2608.00491)
- [Minitap](https://arxiv.org/abs/2602.07787)
- [Situational judgment tests](https://arxiv.org/abs/2510.22170)
- [Chess conceptual alignment](https://arxiv.org/abs/2510.26025)
- [Thinking Beyond Tokens](https://arxiv.org/abs/2507.00951)
- [Inheritune / When Attention Collapses](https://arxiv.org/abs/2404.08634)
- [LiveBench](https://github.com/LiveBench/LiveBench)

Boundary-Bench was not added because the identified paper did not list Ravid
among its authors. The author subsequently confirmed starting at Meta and
ending the Wand AI appointment in August 2025. Those month-level dates are
shown with date labels, without inventing exact days. The NYU end date remains
unconfirmed and is not inferred from the Meta/Wand transition.

Min-p's page uses its verified first-release date (July 1, 2024) rather than
the old January 1, 2025 placeholder. The ICLR 2025 venue and oral status are
shown separately. Its homepage priority is an editorial choice, not a date change.
S-JEPA and HP-JEPA are listed as preprints; the Neural Tokenizer paper is
identified as a workshop paper rather than a main-conference NeurIPS paper.
