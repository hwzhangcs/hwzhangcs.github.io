#!/usr/bin/env sh
# Compile latex/cv.tex (Jake's Resume layout) to assets/hanwen-zhang-cv.pdf.
# Requires Tectonic (https://tectonic-typesetting.github.io) or latexmk with pdfLaTeX.
set -eu
root=$(cd "$(dirname "$0")/.." && pwd)
out=$(mktemp -d)
if command -v tectonic >/dev/null 2>&1; then
  tectonic --outdir "$out" "$root/latex/cv.tex"
else
  latexmk -pdf -interaction=nonstopmode -output-directory="$out" "$root/latex/cv.tex"
fi
cp "$out/cv.pdf" "$root/assets/hanwen-zhang-cv.pdf"
rm -rf "$out"
echo "Wrote $root/assets/hanwen-zhang-cv.pdf"
