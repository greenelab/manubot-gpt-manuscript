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
   export PREV_VER="v02.1"
   export CURR_VER="v03.0"
   ```

1. Tag the current version of the latex file (do not push yet):
   ```bash
   git tag -f ${CURR_VER} <commit hash>
   ```

   To remove a tag:
   ```bash
   git tag -d <tag>
   ```

1. Generate diff between versions and compile (**WARNING**: figure some captions were manually updated):
   ```bash
   mkdir -p diffs
   git show ${PREV_VER}:latex/manuscript.tex > diffs/${PREV_VER}.tex
   git show ${CURR_VER}:latex/manuscript.tex > diffs/${CURR_VER}.tex

   ${LATEXDIFF_PATH} \
     diffs/${PREV_VER}.tex \
     diffs/${CURR_VER}.tex > \
     diffs/diff_${PREV_VER}_vs_${CURR_VER}.tex
   
   latexmk diffs/diff_${PREV_VER}_vs_${CURR_VER}.tex
   ```

1. Check diff pdf and compare with previous and current versions.

1. If everything is ok, add to git:
   ```bash
   git add diffs/diff_${PREV_VER}_vs_${CURR_VER}.tex
   ```

1. Push tags:
   ```bash
   git push origin ${CURR_VER}
   ```
