"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why
the homework got eaten, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

EXCUSE = (
    "The homework said 'show your work,' so I did. "
    "It's in my stomach now. Go ahead, ask me to show it."
)


def check_excuse(line):
    """The excuse must be one non-blank line of 1 to 200 chars."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("excuse must not be blank")
    if "\n" in stripped or len(stripped) > 200:
        raise ValueError("excuse must be one line of at most 200 chars")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(check_excuse(EXCUSE))


if __name__ == "__main__":
    main()
