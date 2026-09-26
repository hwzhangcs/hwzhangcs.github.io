# Maintaining the academic homepage

## Sources of truth

- `_pages/about.md`: short introduction and research opportunity statement.
- `_pages/cv.md`: education, activities, service and skills; update `updated` only when CV content changes.
- `_data/research.yml`: research facts. `selected: true` includes a record on the homepage; `details` appear only in the CV. Keep unknown dates and affiliations absent.
- `_data/publications.yml`: exact titles, author order, publication metadata, contribution and DOI. Rendered consistently on the homepage, Publications and CV.
- `_portfolio/*.md`: project facts and detail pages. `purpose`, `contribution`, `stack`, `code_url`, optional `year` and `order` also power project lists and the CV. Only use verified repository links.
- `_pages/bone-to-shape.md`: research overview and progress, linked from the home and CV.
- `assets/diagrams/`: original, explicitly labeled workflow schematics, not experimental figures.
- `_includes/featured-research.html` and `_includes/featured-software.html`: image-and-text homepage highlights.
- `_includes/hanwen-ip.md` and `_includes/hanwen-awards.md`: intellectual property and honors.

The previous JSON CV is preserved in `templates/legacy-cv.json` as a historical snapshot, excluded from publication. It is not a second editable source. `scripts/update_cv_json.sh` intentionally refuses to regenerate it. Old CV URLs redirect to `/cv/`.

## Presentation

Public pages use `_layouts/academic.html`, with the AcademicPages base styles and `_sass/layout/_academic.scss` overrides. Main navigation and the profile remain consistent across pages. The breakpoint for compact navigation/profile is 1024px.

`assets/js/academic.js` handles only menu, theme, section state and printing. Normal pages do not load the previous 4.4 MB JavaScript bundle. Set `math: true`, `mermaid: true` or `plotly: true` on a page only when its content uses that library. Plotly pages must initialize their own plots.

Print the CV using its Print / Save as PDF button. Supplemental grades expand during printing and return to their previous state afterwards.

## Publication hygiene

Template examples, sample attachments, unused archive pages and maintenance files are excluded in `_config.yml`. Sample sources are retained in the repository. No blog feed is advertised until there is a real blog to publish. GitHub Pages may still generate an empty feed; it must contain no sample posts.

Build with `bundle exec jekyll build`, then run `python3 scripts/check_site.py _site`. Check responsive layout at 375, 768, 1024 and 1440px, dark mode, keyboard navigation, and CV printing after layout changes.
