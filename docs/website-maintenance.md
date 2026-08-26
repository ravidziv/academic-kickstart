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
- Podcast: `content/home/podcast.md`.
- Experience: `content/home/experience.md`. Use `date_label` when exact dates
  are unavailable; only confirmed current roles should have `current = true`.
- Publications: each `content/publication/<slug>/` folder contains the page
  and its `cite.bib`. Preserve existing slugs when updating a paper.
- Selected research: six papers have `featured: true`. Recent Publications
  excludes these so entries are not repeated.
- `content.pinned` in `content/home/featured.md` puts Layer by Layer and Min-p
  first without changing their dates. The remaining selected papers follow in
  descending date order. Every pinned page must exist and be featured.

The homepage presents research alongside practical methods, benchmarks, and
systems. Project descriptions refer to collaborative work; they do not assert
undocumented product deployments or sole ownership.

The profile's `interests` list also drives the homepage topic labels. World
models, memory, and compression are the leading themes; continual learning
remains an explicit research interest. The user confirmed the current
affiliation as Meta Superintelligence Labs (MSL), the former Assistant Professor
appointment at NYU, Ph.D. supervision by Tali Tishby, postdoctoral research with
Yann LeCun, and advisory work with startups and companies.

`identity: true` on a social profile includes it in `Person.sameAs`. Do not use
this flag for an employer's general website or a podcast's homepage.

Update `lastmod` in `content/_index.md` when the homepage changes meaningfully.
Preserve actual publication dates; do not refresh them to make papers look new.

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
among its authors. The Meta start date and NYU/Wand end dates were not guessed.

Min-p's page uses its verified first-release date (July 1, 2024) rather than
the old January 1, 2025 placeholder. The ICLR 2025 venue and oral status are
shown separately. Its homepage priority is an editorial choice, not a date change.
S-JEPA and HP-JEPA are listed as preprints; the Neural Tokenizer paper is
identified as a workshop paper rather than a main-conference NeurIPS paper.
