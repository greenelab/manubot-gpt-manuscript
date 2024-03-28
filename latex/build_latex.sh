#!/bin/bash
set -e

latexmk -shell-escape

# split
pdftk manuscript.pdf cat 1-16 output manuscript-main_text.pdf
pdftk manuscript.pdf cat 17-end output manuscript-supplementary_information.pdf

# rm manuscript.pdf

mv manuscript-main_text.pdf "Manuscript - Manubot AI Editor - v03.0.pdf"
mv manuscript-supplementary_information.pdf "Supplementary Material - Manubot AI Editor - v03.0.pdf"
