#!/usr/bin/env python3
"""Regenerate scripts/horneroctl-commands.txt from horneroctl help text.

The CLI has no machine-readable command tree, so this parses the usage
strings in HorneroOS/hornero `cli/modules/hornero_cli/help.v`:

    git -C ../hornero show origin/main:cli/modules/hornero_cli/help.v \
        > /tmp/help.v
    scripts/gen-horneroctl-commands.py /tmp/help.v <hornero-sha> \
        > scripts/horneroctl-commands.txt

Each output line is one valid command path (`appearance theme set`).
"""
import re
import sys

WORD = re.compile(r"^[a-z][a-z0-9-]*$")


def main() -> int:
    src = open(sys.argv[1], encoding="utf-8").read()
    ref = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    paths: set[str] = set()

    # Top-level commands: the "Commands:" table in root_help().
    root = src.split("Commands:", 1)[1].split("Global flags:", 1)[0]
    for line in root.splitlines():
        m = re.match(r"^  ([a-z][a-z0-9-]*)\s", line)
        if m:
            paths.add(m.group(1))

    # Per-command blocks: `'name' { return 'Usage: ...' }`.
    for m in re.finditer(r"^\t\t'([a-z][a-z -]*)' \{\n(.*?)^\t\t\}",
                         src, re.S | re.M):
        name, body = m.group(1), m.group(2)
        paths.add(name)
        usage = re.search(r"Usage: horneroctl ([^\n]*)", body)
        rest = usage.group(1)[len(name):] if usage else ""
        alt = re.match(r"\s*[<\[]([a-z0-9|*-]+)[>\]]", rest)
        verbs = alt.group(1).split("|") if alt else []
        verbs = [v for v in verbs if v not in ("true", "false")
                 and not v.startswith("-")]
        is_group = len(verbs) > 1 or rest.lstrip().startswith("<verb>")
        if not is_group:
            continue
        for verb in verbs:
            if WORD.match(verb):
                paths.add(f"{name} {verb}")
        # Indented verb table (two-space indent, lowercase verb first).
        table = body.split("\n\n", 1)[1] if "\n\n" in body else ""
        table = re.split(r"\n(?:Options|Examples|Exit codes)", table)[0]
        for line in table.splitlines():
            vm = re.match(r"^  ([a-z][a-z0-9-]*)(?:\s|$)", line)
            if vm:
                paths.add(f"{name} {vm.group(1)}")

    print(f"# horneroctl command paths, generated from HorneroOS/hornero@{ref}")
    print("# cli/modules/hornero_cli/help.v by scripts/gen-horneroctl-commands.py")
    for p in sorted(paths):
        print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
