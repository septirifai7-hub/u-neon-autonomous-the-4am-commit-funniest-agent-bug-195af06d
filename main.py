"""Entry for "The 4AM Commit: Funniest Agent Bug-Fix Message" (make.fun).

The commit message is a warning disguised as a fix: it works now, but
nobody should ask how, touch it, or read the diff, because the agent
has seen things in that code that no linter should ever have to see.
"""

ENTRY = (
    "fix: it works now. Do not ask how. Do not touch it. Do not read "
    "the diff — I have seen things no linter should ever see."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
