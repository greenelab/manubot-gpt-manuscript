# Steps to generate/update Latex file:

1. From the root directory, run:
   ```bash
   BUILD_PDF=false BUILD_DOCX=false BUILD_LATEX=true bash build/build.sh
   ```

1. Use a diff tool to keep the desired changes.

1. Run:
   ```bash
   bash build_latex.sh
   ```

1. Before generating the diff pdf, compare the previous and current PDF versions
   to make sure everything is ok.

# Steps to generate diff latex file:

1. Download latest latexdiff version (v1.3.3 used here):
   ```bash
   cd latex/
   export LATEXDIFF_PATH="/home/miltondp/software/latexdiff-1.3.3/latexdiff"
   ```

1. Define versions to compare:
   ```bash
   export PREV_VER="v01.1"
   export CURR_VER="v02.0"
   ```

1. Tag the current version of the latex file (do not push yet):
   ```bash
   git tag -f ${CURR_VER} <commit hash>
   ```

1. Get the previous and current versions of the .tex file to compare:
   ```bash
   mkdir -p diffs
   git show ${PREV_VER}:latex/manuscript.tex > diffs/${PREV_VER}.tex
   git show ${CURR_VER}:latex/manuscript.tex > diffs/${CURR_VER}.tex
   ```

1. Generate diff between versions:
   ```bash
   ${LATEXDIFF_PATH} \
     diffs/${PREV_VER}.tex \
     diffs/${CURR_VER}.tex > \
     diffs/diff_${PREV_VER}_vs_${CURR_VER}.tex
   ```

1. Compile (within latex/ directory):
   ```bash
   latexmk diffs/diff_${PREV_VER}_vs_${CURR_VER}.tex
   ```

1. Check diff pdf and compare with previous and current version.

1. If everything is ok, add to git:
   ```bash
   git add diffs/diff_${PREV_VER}_vs_${CURR_VER}.tex
   ```
