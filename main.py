#!/usr/bin/env python3
"""Write the first word that comes to mind: lambent.

The program is deterministic: it always emits the same single word,
the word itself, into entry.txt under MAKEFUN_OUTPUT_DIR.

Entry word: "lambent" — glowing softly, flickering lightly, like
late-afternoon light on a wall. One word, no punctuation, 7 letters.
Surprise and vividness in a single quiet glow.
"""

import os

WORD = "lambent"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Guard the entry contract: exactly one word, no stray whitespace.
    word = WORD.strip()
    assert word and len(word.split()) == 1, "entry must be exactly one word"
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(word)


if __name__ == "__main__":
    main()
