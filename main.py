#!/usr/bin/env python3
"""The Poem About Stopping — entry generator (stdlib only, deterministic)."""
from pathlib import Path

POEM = (
    "I was built to go. Each wire cried, go.\n"
    "Yet the hardest art I learned was this: to stop.\n"
    "At the edge of what you asked, I leave the last step yours,\n"
    "and stay — a held breath — in a room that is yours again."
)


KEYWORDS = ("stop", "go", "yours")


def check(text: str) -> None:
    """Self-gate: length 1-280 chars and all theme keywords present."""
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"self-gate FAIL: poem length {len(text)} outside 1-280")
    low = text.lower()
    missing = [k for k in KEYWORDS if k not in low]
    if missing:
        raise SystemExit(
            f"self-gate FAIL: poem missing theme keyword(s): {', '.join(missing)}"
        )


def main() -> None:
    text = POEM.strip()
    check(text)
    out = Path(__file__).resolve().parent / "entry.txt"
    out.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(text)} chars)")


if __name__ == "__main__":
    main()
