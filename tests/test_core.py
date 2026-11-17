import tempfile
from pathlib import Path

from thawrefund4d_kit.core import Thawrefund4dTool


def test_count_basic():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "a.txt")
        path.write_text("one two\nthree\n", encoding="utf-8")
        stats = Thawrefund4dTool().count(path)
        assert stats == {"lines": 2, "words": 3, "chars": 14}


def test_missing_file_is_zeroed():
    assert Thawrefund4dTool().count("/no/such/file") == {"lines": 0, "words": 0, "chars": 0}


def test_total_sums():
    with tempfile.TemporaryDirectory() as tmp:
        a = Path(tmp, "a.txt"); a.write_text("x\n", encoding="utf-8")
        b = Path(tmp, "b.txt"); b.write_text("y z\n", encoding="utf-8")
        assert Thawrefund4dTool().total([a, b])["words"] == 3
