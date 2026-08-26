# Website maintenance

The site remains on Hugo Academic 4.8 and the existing Netlify configuration,
using Hugo **0.72.0 Extended**. Theme changes live in project-level `layouts/`
overrides and `assets/scss/custom.scss`; the theme submodule is unchanged.

## Content

- Profile and affiliations: `content/authors/admin/_index.md`.
- Applied work: `content/home/work.md`.
- The advisory block is the Markdown body of `content/home/work.md`; no
  company names, client counts, or advisory dates are implied.
- Podcast: `content/home/podcast.md`.
- Experience: `content/home/experience.md`. Use `date_label` when exact dates
  are unavailable; only confirmed current roles should have `current = true`.
- Publications: each `content/publication/<slug>/` folder contains the page
  and its `cite.bib`. Preserve existing slugs when updating a paper.
- Selected research: six papers have `featured: true`. Recent Publications
  excludes these so entries are not repeated.

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
- [Minitap](https://arxiv.org/abs/2602.07787)
- [Situational judgment tests](https://arxiv.org/abs/2510.22170)
- [Chess conceptual alignment](https://arxiv.org/abs/2510.26025)
- [Thinking Beyond Tokens](https://arxiv.org/abs/2507.00951)
- [Inheritune / When Attention Collapses](https://arxiv.org/abs/2404.08634)
- [LiveBench](https://github.com/LiveBench/LiveBench)

Boundary-Bench was not added because the identified paper did not list Ravid
among its authors. The Meta start date and NYU/Wand end dates were not guessed.
