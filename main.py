"""Write one joke about demoing beside an AI coding agent.

The program holds a single one-line joke, checks it fits the
1-280 character limit, writes it to ``entry.txt`` in the output
directory, and verifies the bytes on disk match the joke exactly.
"""

import os
import sys

TEXT = (
    "I asked my AI agent to fix one bug. It rewrote the whole file, "
    "renamed the bug, and promoted it \u2014 now the bug is reviewing my PRs."
)


def main() -> int:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        print(
            f"joke must be 1-280 characters and non-blank, got {len(TEXT)}",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)

    with open(entry_path, "r", encoding="utf-8") as handle:
        if handle.read() != TEXT:
            print("entry.txt on disk differs from the joke text", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
