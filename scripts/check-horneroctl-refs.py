#!/usr/bin/env python3
"""Fail when docs reference a horneroctl command path that does not exist.

Scans Markdown code only (fenced blocks and inline code spans, so prose
such as "horneroctl and ..." is ignored) for `horneroctl <group> <verb>`
and checks the command words against scripts/horneroctl-commands.txt
(generated from the CLI help text by scripts/gen-horneroctl-commands.py).

- Words are consumed while the path so far is a group; the first
  non-group word ends the command and the rest are arguments.
- Inline code spans may wrap across lines; line numbers point at the
  `horneroctl` token.
- Inside inline code, verb alternations are validated one by one:
  `theme set|apply` and `theme list | show <id> | get`. In fenced
  blocks a `|` is a shell pipe and ends the command.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIST = ROOT / "scripts" / "horneroctl-commands.txt"
WORD = re.compile(r"^[a-z][a-z0-9-]*$")
FENCE = re.compile(r"^(```|~~~)[^\n]*\n(.*?)^\1[ \t]*$", re.S | re.M)
INLINE = re.compile(r"(?<!`)`([^`]+?)`(?!`)", re.S)
CMD = re.compile(r"\bhorneroctl\b(?!-)")


def load_paths() -> tuple[set[str], set[str]]:
    """Return (all valid paths, paths that have sub-verbs)."""
    paths = {
        line.strip()
        for line in LIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    groups = {p.rsplit(" ", 1)[0] for p in paths if " " in p}
    return paths, groups


def resolve(tokens: list[str], groups: set[str]) -> list[str]:
    """Consume command words from tokens; flags are skipped."""
    words: list[str] = []
    for tok in tokens:
        if tok.startswith("-"):
            continue
        if not WORD.match(tok):
            break
        words.append(tok)
        if " ".join(words) not in groups:
            break
    return words


def candidates(text: str, inline: bool, groups: set[str]) -> list[str]:
    """Expand one command's text (after `horneroctl`) into command paths."""
    if not inline:
        text = text.split("|", 1)[0]  # shell pipe in a code block
        return [" ".join(w) for w in [resolve(text.split(), groups)] if w]
    segments = re.split(r"\s+\|\s+", text.strip())
    first = segments[0].split()
    # Expand inline `a|b` alternations inside the first segment.
    out: list[str] = []
    stack = [first]
    while stack:
        toks = stack.pop()
        for i, tok in enumerate(toks):
            if "|" in tok and all(WORD.match(p) for p in tok.split("|")):
                for alt in tok.split("|"):
                    stack.append(toks[:i] + [alt] + toks[i + 1:])
                break
        else:
            words = resolve(toks, groups)
            if words:
                out.append(" ".join(words))
    # `list | show <id> | get`: each later segment names a sibling verb.
    if out and len(segments) > 1:
        parent = out[0].rsplit(" ", 1)[0] if " " in out[0] else ""
        for seg in segments[1:]:
            toks = seg.split()
            if toks and WORD.match(toks[0]):
                out.append(f"{parent} {toks[0]}".strip())
    return out


def scan(text: str, paths: set[str], groups: set[str], rel: str) -> tuple[int, int]:
    """Check one file; return (references checked, unknown references)."""
    checked = errors = 0
    snippets: list[tuple[int, str, bool]] = []
    masked = list(text)
    for m in FENCE.finditer(text):
        body_start = m.start(2)
        for line in m.group(2).split("\n"):
            snippets.append((body_start, line, False))
            body_start += len(line) + 1
        masked[m.start():m.end()] = [
            c if c == "\n" else " " for c in text[m.start():m.end()]
        ]
    plain = "".join(masked)
    for m in INLINE.finditer(plain):
        if "\n\n" not in m.group(1):
            snippets.append((m.start(1), m.group(1), True))
    for offset, snippet, inline in snippets:
        for m in CMD.finditer(snippet):
            rest = snippet[m.end():]
            for cmd in dict.fromkeys(candidates(rest, inline, groups)):
                checked += 1
                if cmd not in paths:
                    lineno = text.count("\n", 0, offset + m.start()) + 1
                    print(f"{rel}:{lineno}: unknown command `horneroctl {cmd}`")
                    errors += 1
    return checked, errors


def main() -> int:
    """Scan every Markdown file under the repo root."""
    paths, groups = load_paths()
    checked = errors = 0
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        c, e = scan(md.read_text(encoding="utf-8"), paths, groups,
                    str(md.relative_to(ROOT)))
        checked += c
        errors += e
    print(f"checked {checked} horneroctl reference(s), {errors} unknown")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
