"""Entry for news-image-20261125: copy the pre-rendered image to the output dir.

The image (entry.png, 1024x1024, 54 verified stories from Wednesday
25 November 2026) is rendered at build time and shipped in this repository.
This program only copies it, so it runs with the standard library alone,
needs no network, and writes identical bytes on every run.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing from repository root")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
    sys.exit(0)
