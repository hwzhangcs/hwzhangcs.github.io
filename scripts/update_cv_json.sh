#!/bin/sh
# The website no longer uses a parallel JSON CV. See docs/content-maintenance.md.
printf '%s\n' 'Legacy JSON CV generation is disabled. Edit _pages/cv.md and the shared research/publication data instead.' >&2
exit 1
