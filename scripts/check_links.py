"""Fail if any relative Markdown link points to a file that does not exist."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
ROOT = Path(__file__).resolve().parent.parent


def broken_links(md_file: Path) -> list[str]:
    errors = []
    for target in LINK.findall(md_file.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("mailto:"):
            continue
        if not (md_file.parent / target).resolve().exists():
            errors.append(f"{md_file.relative_to(ROOT)}: {target}")
    return errors


def main() -> int:
    files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    errors = [e for f in files for e in broken_links(f)]
    for e in errors:
        print(f"broken link: {e}")
    print(f"checked {len(files)} files, {len(errors)} broken links")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
