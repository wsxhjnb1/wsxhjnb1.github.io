# Yuhao Xie · 谢雨豪

Personal academic website: **https://wsxhjnb1.github.io/**

- English: `/`
- 中文：`/zh/`
- Résumé source of record: [wsxhjnb1/resume](https://github.com/wsxhjnb1/resume)

The site is plain HTML, CSS and SVG, hosted on GitHub Pages. It does not require
a package manager, build service, external fonts, analytics, or a server backend.
Navigation, language switching, PDF downloads and teaching details work without
JavaScript.

## Update

Edit the English/Chinese text and page template in `tools/build_site.py`, then:

```sh
python tools/build_site.py
python -m http.server 8765
```

Open `http://localhost:8765/` and `http://localhost:8765/zh/`.
Edit `assets/styles.css` for layout changes. The conceptual inference-stack
illustration is an inline SVG, not an experimental result.

Copy the latest approved PDFs from the résumé repository to `assets/resume/`
when updating the downloads. Preserve the résumé filenames so public links stay
stable. The initial copies exactly match the 2026-11-05 résumé release.

GitHub Pages publishes the root of the `main` branch. `.nojekyll` keeps this a
static deployment. Push the generated HTML alongside source updates.
