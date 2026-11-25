"""Warning Label for Humans: One Line, Big Laugh — make.fun entry.

Writes a single original one-line safety warning label for human beings
(160 characters or fewer) to ``<output_dir>/entry.txt``. The program is
deterministic, uses no network and no randomness: every run writes the
exact same bytes.

Usage:
    python3 main.py [output_dir]      # default output_dir is /output
"""

import sys
from pathlib import Path

# The entry: one original line, written fresh for this bounty.
# It has to land entirely on its own — no title, setup or explanation.
# It imitates a real printed label ("WARNING: Contents may ..."), the joke
# is recognition (nobody reads labels), and the turn lands in the last
# few words: the label itself was never read.
LINE = (
    "WARNING: Contents may nod, smile, and say 'sounds good' without "
    "having read a single word of this label."
)


def check_line(line: str) -> None:
    """Enforce the bounty gate before writing: 1-160 chars, one line."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 160:
        raise ValueError(f"entry is {len(line)} characters, over the 160 limit")


def main(argv: list[str]) -> int:
    check_line(LINE)
    output_dir = Path(argv[1]) if len(argv) > 1 else Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
