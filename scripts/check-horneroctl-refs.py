#!/usr/bin/env python3
"""Fail when docs reference a horneroctl command path that does not exist.

Scans every Markdown file for `horneroctl <group> <verb> ...` and checks
the command words against scripts/horneroctl-commands.txt (generated from
the CLI help text by scripts/gen-horneroctl-commands.py). Words are
consumed while the path so far is a group; the first non-group word ends
the command and the rest are treated as arguments.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIST = ROOT / "scripts" / "horneroctl-commands.txt"
WORD = re.compile(r"^[a-z][a-z0-9-]*$")
REF = re.compile(r"\bhorneroctl((?:[ \t]+[^\s`|]+)*)")


def main() -> int:
    paths = {
        line.strip()
        for line in LIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    groups = {p.rsplit(" ", 1)[0] for p in paths if " " in p}
    errors = 0
    checked = 0
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        rel = md.relative_to(ROOT)
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for m in REF.finditer(line):
                words = []
                for tok in m.group(1).split():
                    if tok.startswith("-"):
                        continue  # global flags like --json
                    if not WORD.match(tok):
                        break
                    words.append(tok)
                    if " ".join(words) not in groups:
                        break
                if not words:
                    continue  # bare `horneroctl` mention
                cmd = " ".join(words)
                checked += 1
                if cmd not in paths:
                    print(f"{rel}:{lineno}: unknown command `horneroctl {cmd}`")
                    errors += 1
    print(f"checked {checked} horneroctl reference(s), {errors} unknown")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
