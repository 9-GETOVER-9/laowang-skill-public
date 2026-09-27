#!/usr/bin/env python3
"""Fail fast when private or oversized artifacts enter the public Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 10 * 1024 * 1024
REQUIRED = {"SKILL.md", "README.md", "LICENSE", "NOTICE.md"}
FORBIDDEN_NAMES = {
    "source_registry.jsonl",
    "provenance_edges.jsonl",
    "master_manifest.jsonl",
}
FORBIDDEN_SUFFIXES = {
    ".mp3", ".mp4", ".m4a", ".wav", ".srt", ".pkl", ".npy",
    ".sqlite", ".safetensors",
}
FORBIDDEN_TOP_LEVEL = {"corpus", "datasets", "canonical", "raw"}
PRIVATE_PATH_RE = re.compile(r"[A-Za-z]:[\\/](?:Users|文档|桌面)[\\/]", re.IGNORECASE)
LOCAL_REFERENCE_RE = re.compile(
    r"(?<![\w/])(?:modules|references|cases)/[A-Za-z0-9_./-]+\.(?:md|jsonl)"
)


def missing_local_references(root: Path) -> list[str]:
    missing = []
    for document in root.rglob("*.md"):
        if ".git" in document.parts:
            continue
        content = document.read_text(encoding="utf-8")
        for match in LOCAL_REFERENCE_RE.finditer(content):
            reference = match.group()
            if not (root / reference).is_file():
                missing.append(f"missing local reference in {document.relative_to(root)}: {reference}")
    return sorted(set(missing))


def main() -> int:
    errors: list[str] = []
    present = {path.name for path in ROOT.iterdir()}
    for name in sorted(REQUIRED - present):
        errors.append(f"missing required file: {name}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in FORBIDDEN_TOP_LEVEL:
            errors.append(f"forbidden public directory: {rel}")
        if path.name in FORBIDDEN_NAMES:
            errors.append(f"private registry/corpus file: {rel}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden binary/raw suffix: {rel}")
        if path.stat().st_size > MAX_FILE_BYTES:
            errors.append(f"file exceeds 10 MiB: {rel}")
        if path == Path(__file__):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if PRIVATE_PATH_RE.search(text):
            errors.append(f"local absolute path found: {rel}")

    skill = ROOT / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        if not re.search(r"(?m)^name:\s*laowang-skill-public\s*$", text):
            errors.append("SKILL.md name must be laowang-skill-public")

    evidence = ROOT / "references" / "evidence"
    if evidence.exists():
        files = sorted(path.name for path in evidence.iterdir() if path.is_file())
        if files != ["public_evidence_note.jsonl"]:
            errors.append("references/evidence may only contain public_evidence_note.jsonl")

    errors.extend(missing_local_references(ROOT))

    if errors:
        print("Public release validation failed:")
        for error in sorted(set(errors)):
            print(f"- {error}")
        return 1

    file_count = sum(1 for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts)
    print(f"Public release validation passed: {file_count} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
