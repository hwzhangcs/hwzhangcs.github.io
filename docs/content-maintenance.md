# Maintaining the academic homepage

## Sources of truth

- `_includes/hero.html`: name, research statement, background and availability at the top of the homepage.
- `_pages/about.md`: homepage section order (News, Research, Publications, Software).
- `_data/news.yml`: dated news items, newest first. Only confirmed months, and only items with research or academic weight.
- `_data/education.yml`: GPA, rank, averages and courses. Used by the hero, the homepage Education & Honors section and the CV. `home: true` courses appear on the homepage.
- `_data/honors.yml`: all honors for the CV; `home: true` marks the three shown on the homepage.
- `_data/ip.yml`: patents and software copyrights for the CV; `home: true` lists an item under Publications & Patents on the homepage.
- `_pages/cv.md`: education, activities, service and skills; update `updated` only when CV content changes.
- `_data/research.yml`: research facts. `selected: true` includes a record on the homepage; `details` appear only in the CV. Keep unknown dates and affiliations absent.
- `_data/publications.yml`: exact titles, author order, publication metadata, contribution and DOI. Rendered consistently on the homepage, Publications and CV.
- `_portfolio/*.md`: project facts and detail pages; `home: true` lists a project on the homepage. `purpose`, `contribution`, `stack`, `code_url`, optional `year` and `order` also power project lists and the CV. Only use verified repository links.
- `_pages/bone-to-shape.md`: research overview and progress, linked from the home and CV.
- `assets/diagrams/`: original, explicitly labeled workflow schematics, not experimental figures.
- `_includes/featured-research.html` (featured project plus compact research items) and `_includes/featured-software.html` (compact software list).
- `_includes/hanwen-ip.md` and `_includes/hanwen-awards.md`: render the CV lists from `ip.yml` and `honors.yml`.

The previous JSON CV is preserved in `templates/legacy-cv.json` as a historical snapshot, excluded from publication. It is not a second editable source. `scripts/update_cv_json.sh` intentionally refuses to regenerate it. Old CV URLs redirect to `/cv/`.

## Presentation

Public pages use `_layouts/academic.html`, with the AcademicPages base styles and `_sass/layout/_academic.scss` overrides. Every page uses one 760px reading column; the homepage replaces the page title with the hero. Breakpoints are 760px (hero and featured project stack) and 600px (navigation wraps below the name).

`assets/js/academic.js` handles only theme, homepage section state and printing. Normal pages do not load the previous 4.4 MB JavaScript bundle. Set `math: true`, `mermaid: true` or `plotly: true` on a page only when its content uses that library. Plotly pages must initialize their own plots.

The CV page links to `assets/hanwen-zhang-cv.pdf`. After any CV change, rebuild the site and run `node scripts/build_cv_pdf.js _site` to regenerate the PDF from the print styles, then commit it. Build with `--config _config.yml,_config_docker.yml` so stylesheet URLs resolve locally. Supplemental grades expand during printing.

## Publication hygiene

Template examples, sample attachments, unused archive pages and maintenance files are excluded in `_config.yml`. Sample sources are retained in the repository. No blog feed is advertised until there is a real blog to publish. GitHub Pages may still generate an empty feed; it must contain no sample posts.

Build with `bundle exec jekyll build`, then run `python3 scripts/check_site.py _site`. Check responsive layout at 375, 768, 1024 and 1440px, dark mode, keyboard navigation, and CV printing after layout changes.

## Homepage hierarchy

1. Primary: research statement, Bone-to-Shape, research internships.
2. Secondary: rank and GPA (hero credential line), publication and patent, three selected honors, top courses.
3. Supporting (CV only): lesser scholarships and titles, MCM, CCF CSP, CET-6, exchange programs, service roles other than the AI Club, skills, course and game projects.
