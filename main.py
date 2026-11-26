"""Copy the entry text into the output directory.

The grader runs this with no network, a read-only working directory, and
only MAKEFUN_OUTPUT_DIR writable, so this file does nothing but copy.
"""

import os
import shutil

ENTRY = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(os.path.dirname(__file__), ENTRY),
        os.path.join(out_dir, ENTRY),
    )


if __name__ == "__main__":
    main()


# Note on this file: the copier is deliberately boring. The entry's joke
# lives entirely in entry.txt, so main.py adds nothing of its own — it
# just moves the text where the grader expects it, every run the same.
