# hwzhangcs.github.io

Source for [hwzhangcs.github.io](https://hwzhangcs.github.io), the academic homepage of Hanwen Zhang (张瀚文).
It is a Jekyll site published by GitHub Pages from the `main` branch.

## Layout

| Path | Contents |
|---|---|
| `_data/` | Facts shown on the site: news, research, publications, patents, education, honors, navigation |
| `_pages/` | Homepage (`about.md`), CV, Bone-to-Shape project page, publications, software, sitemap, 404 |
| `_portfolio/` | Software project pages |
| `_includes/`, `_layouts/` | Page templates |
| `_sass/` | Styles: `_base.scss` (element defaults) and `_academic.scss` (site design) |
| `assets/` | Compiled CSS entry, JavaScript, self-hosted Source Serif 4, diagrams, PDF CV |
| `images/` | Portrait and favicons |
| `latex/cv.tex` | LaTeX source of the PDF CV (Jake's Resume layout) |
| `scripts/` | Site checks and the CV build |
| `docs/` | Maintenance notes, design decisions and facts to verify |

## Local preview

With Ruby and Bundler:

```bash
bundle install
bundle exec jekyll serve --config _config.yml,_config_docker.yml
```

Or with Docker: `docker compose up`, or open the folder in the VS Code Dev Container. The site is served at http://localhost:4000.

## Checks

```bash
bundle exec jekyll build
python3 scripts/check_site.py _site   # links, anchors, headings, canonical URLs, published files
python3 scripts/check_cv_tex.py       # one-page LaTeX CV core facts agree with _data/
./scripts/build_cv_pdf.sh             # rebuild assets/hanwen-zhang-cv.pdf (Tectonic or latexmk)
```

See [docs/content-maintenance.md](docs/content-maintenance.md) for what to edit when content changes.

## Credits

Originally based on [AcademicPages](https://github.com/academicpages/academicpages.github.io), itself derived from
[Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) (MIT, see `LICENSE`).
Icons are from [Font Awesome Free](https://fontawesome.com) (CC BY 4.0); the typeface is
[Source Serif 4](https://github.com/adobe-fonts/source-serif) (SIL OFL 1.1, see `assets/fonts/`);
the PDF CV layout is [Jake's Resume](https://github.com/jakegut/resume) (MIT).
