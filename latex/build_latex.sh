#!/bin/bash
set -e

latexmk -shell-escape

# split
pdftk manuscript.pdf cat 1-15 output manuscript-main_text.pdf
pdftk manuscript.pdf cat 16-end output manuscript-supplementary_information.pdf

# rm manuscript.pdf
