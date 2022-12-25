#!/usr/bin/env python

from pathlib import Path

from chatgpt_editor.editor import ManuscriptEditor
from chatgpt_editor.models import GPT3CompletionModel

if __name__ == "__main__":
    # create a manuscript editor and model to revise
    me = ManuscriptEditor(
        content_dir="content",
    )

    model = GPT3CompletionModel(
        title=me.title,
        keywords=me.keywords,
    )

    # revise the manuscript
    output_folder = (Path("tmp") / "chatgpt-editor-output").resolve()
    output_folder.mkdir(parents=True, exist_ok=True)

    me.revise_manuscript(output_folder, model, debug=True)

    # move the revised manuscript back to the content folder
    for f in output_folder.glob("*"):
        f.rename(me.content_dir / f.name)

    # remove output folder
    output_folder.rmdir()
