"""Count lines, words and characters in text files."""
from __future__ import annotations

from pathlib import Path

VERSION = "0.9.5"


class Thawrefund4dTool:
    """wc-like statistics with a stable shape."""

    def count(self, path):
        target = Path(path)
        if not target.is_file():
            return {"lines": 0, "words": 0, "chars": 0}
        text = target.read_text(encoding="utf-8", errors="replace")
        return {"lines": len(text.splitlines()),
                "words": len(text.split()),
                "chars": len(text)}

    def total(self, paths):
        acc = {"lines": 0, "words": 0, "chars": 0}
        for path in paths:
            for key, value in self.count(path).items():
                acc[key] += value
        return acc
