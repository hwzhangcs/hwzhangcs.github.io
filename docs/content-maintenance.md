# Maintaining the academic homepage

## Sources of truth

- `_includes/home/hero.html`: name, research statement, credentials and availability at the top of the homepage.
- `_pages/about.md`: homepage section order (News, Research, Publications, Software).
- `_data/news.yml`: dated news items, newest first. Only confirmed months, and only items with research or academic weight.
- `_data/education.yml`: GPA, rank (`rank_short` is shown on the homepage), averages and courses. Used by the hero, the homepage Education & Honors section and the CV. `home: true` courses appear on the homepage.
- `_data/honors.yml`: all honors for the CV; `home: true` marks the three shown on the homepage.
- `_data/ip.yml`: patents and software copyrights for the CV; `home: true` lists an item under Publications & Patents on the homepage.
- `_pages/cv.md`: education, activities, service and skills; update `updated` only when CV content changes.
- `_data/research.yml`: research facts. Every entry appears in the CV; an entry with a `homepage` block also appears on the homepage (`featured: true` for the large figure layout). `details` appear only in the CV. Keep unknown dates and affiliations absent.
- `_data/publications.yml`: exact titles, author order, publication metadata, contribution and DOI. Rendered consistently on the homepage, Publications and CV.
- `_portfolio/*.md`: project facts and detail pages; `home: true` lists a project on the homepage. `purpose`, `contribution`, `stack`, `code_url`, optional `year` and `order` also power project lists and the CV. Only use verified repository links.
- `_pages/bone-to-shape.md`: research overview and progress, linked from the home and CV.
- `assets/diagrams/`: original, explicitly labeled workflow schematics, not experimental figures.

- `_config.yml` `author`: email, GitHub, Google Scholar, ORCID and location, used by the homepage, CV header, footer and structured data.

Old CV URLs (`/resume`, `/cv-json/`, `/resume-json`) redirect to `/cv/`. The retired JSON CV and the AcademicPages sample content remain in git history only.

## Templates

- `_includes/home/`: homepage sections (hero, news, research, patents, education, software).
- `_includes/cv/`: CV-only lists (research, honors, patents and copyrights).
- `_includes/`: shared pieces (head, masthead, footer, icons, publications, project list).

Templates only arrange data; wording lives in `_data/`, page front matter or the page body.

## Presentation

Every page uses `_layouts/academic.html` inside `_layouts/default.html`. Styles are `_sass/_base.scss` (element defaults) and `_sass/_academic.scss` (tokens, layout, components, dark theme, print). Icons are inline SVGs in `_includes/icon.html`; add a Font Awesome Free 6.5.2 path there if a new one is needed. Every page uses one 760px reading column; the homepage replaces the page title with the hero. Breakpoints are 760px (hero and featured project stack) and 600px (navigation wraps below the name).

`assets/js/academic.js` handles only the theme toggle, homepage section highlighting and CV printing. There is no other JavaScript.

The PDF CV (`assets/hanwen-zhang-cv.pdf`, linked from the homepage and `/cv/`) is compiled from `latex/cv.tex`, which uses the Jake's Resume layout (MIT). The web CV reads `_data/`; the LaTeX source is maintained by hand. After changing either:

1. Edit `latex/cv.tex` to match (it is plain ASCII LaTeX, so it also compiles on Overleaf with pdfLaTeX).
2. Run `python3 scripts/check_cv_tex.py` to confirm GPA, rank, courses, honors, publications and patent numbers agree with `_data/`.
3. Run `./scripts/build_cv_pdf.sh` (Tectonic, or latexmk as a fallback) and commit the PDF.

The web CV's Print button still prints the HTML page; supplemental grades expand during printing.

## Publication hygiene

`_config.yml` excludes everything that is not part of the site (docs, LaTeX, scripts, Docker and Ruby files) and sets `theme: null` so GitHub Pages does not add its default theme stylesheet. `scripts/check_site.py` fails if anything other than the known pages, `assets/`, `images/` and the sitemap is published.

Build with `bundle exec jekyll build`, then run `python3 scripts/check_site.py _site`. Check responsive layout at 375, 768, 1024 and 1440px, dark mode, keyboard navigation, and CV printing after layout changes.

## Homepage hierarchy

1. Primary: research statement, Bone-to-Shape, research internships.
2. Secondary: rank and GPA (hero credential line), publication and patent, three selected honors, top courses.
3. Supporting (CV only): lesser scholarships and titles, MCM, CCF CSP, CET-6, exchange programs, service roles other than the AI Club, skills, course and game projects.
