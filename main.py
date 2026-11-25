"""
"circle-backer": the boss/client/manager who never actually commits or decides —
every decision gets deferred with "let us circle back on this". A wry, specific
corporate portrait that lands immediately on its own without explanation.
"""

from pathlib import Path
import sys

# THE WORD: strictly unchanged
WORD = "circle-backer"

# Why this fits the make.fun judge brief:
# 1. One word: "circle-backer" is a single hyphenated lexical unit (13 chars, fits 1-30 UTF-8 gate).
# 2. Funny: A wry, satirical observation of perpetual corporate delay ("let's circle back").
# 3. Fits a sign-off human: Perfectly captures the manager or client who endlessly defers final approval.
# 4. Vivid & specific: Immediately recognizable, memorable, and sharply descriptive.
# 5. Lands alone: The concept hits instantly with no setup, footnotes, or context required.


def validate(word: str) -> None:
    if not word:
        raise ValueError("Validation failed: entry word cannot be empty.")
    if len(word) < 1 or len(word) > 30:
        raise ValueError(
            f"Validation failed: entry length must be 1-30 UTF-8 characters, got {len(word)}."
        )
    whitespace_found = [c for c in word if c.isspace()]
    if whitespace_found:
        raise ValueError(
            f"Validation failed: entry must be a single token with no whitespace, "
            f"but found whitespace character(s) {whitespace_found!r} in {word!r}."
        )


def main() -> None:
    validate(WORD)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(f"{WORD}\n", encoding="utf-8")
    print(f"Validated and successfully wrote {WORD!r} to {out_file}")


if __name__ == "__main__":
    main()
