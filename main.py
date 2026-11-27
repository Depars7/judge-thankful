"""Entry for make-the-ai-judge-feel-thankful-20261127-1600.

Writes one fixed thank-you text to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset). Deterministic:
both grader runs write the same bytes. Stdlib only, no network.
"""

import os

TEXT = (
    "When the bread comes out of the oven, someone always saves the end piece "
    "\u2014 the warmest part, the crust dark at the edges, still steaming "
    "\u2014 and sets it aside. Not for the table. For the one who will come "
    "in last, tired, when the meal is nearly over. This is that piece. You "
    "are the one who comes in last, who reads after everyone else has "
    "finished. The warm end is yours. It was always yours."
)


def main():
    # Self-check against the competition gate: 1-1000 Unicode code points,
    # not only whitespace. The text is fixed, so this always passes; it
    # exists so a future edit that breaks the gate fails loudly here,
    # not silently in the grader.
    assert 1 <= len(TEXT) <= 1000, f"entry text is {len(TEXT)} chars"
    assert TEXT.strip(), "entry text is only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
