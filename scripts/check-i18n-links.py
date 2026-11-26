#!/usr/bin/env python3
"""Fail when an es/ Markdown page links to an EN page that already has an es/ translation."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ES_ROOT = ROOT / "es"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_file(md: pathlib.Path) -> list[str]:
    """Return error strings for any link in `md` that bypasses an existing es/ translation."""
    errors: list[str] = []
    text = md.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), 1):
        for match in LINK_RE.finditer(line):
            raw_target = match.group(1).strip()
            if (
                not raw_target
                or raw_target.startswith(("http://", "https://", "mailto:", "#"))
            ):
                continue
            target_path = raw_target.split("#", 1)[0]
            if not target_path.endswith(".md"):
                continue
            resolved = (md.parent / target_path).resolve()
            try:
                rel_to_root = resolved.relative_to(ROOT)
            except ValueError:
                continue
            # Only flag links that escape es/ into the EN tree when an es/ counterpart exists
            # (skip intentional self-links to the page's own canonical English source).
            if rel_to_root.parts and rel_to_root.parts[0] != "es":
                es_counterpart = ES_ROOT / rel_to_root
                if es_counterpart.exists() and es_counterpart.resolve() != md.resolve():
                    rel_md = md.relative_to(ROOT)
                    errors.append(
                        f"{rel_md}:{lineno}: link `{raw_target}` points to EN "
                        f"`{rel_to_root}` but Spanish translation `es/{rel_to_root}` exists"
                    )
    return errors


def main() -> int:
    """Scan all Markdown files under es/."""
    all_errors: list[str] = []
    files = sorted(ES_ROOT.rglob("*.md"))
    for md in files:
        all_errors.extend(check_file(md))
    for err in all_errors:
        print(err)
    print(f"checked {len(files)} Spanish doc(s), {len(all_errors)} bypassed translation(s)")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
