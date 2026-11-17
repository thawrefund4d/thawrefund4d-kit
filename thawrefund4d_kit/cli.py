"""Command line entry point for thawrefund4d_kit."""
import argparse

from .core import Thawrefund4dTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="count lines and words")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args(argv)
    counter = Thawrefund4dTool()
    for path in args.files:
        stats = counter.count(path)
        print(f"{stats['lines']:>7} {stats['words']:>7} {stats['chars']:>8}  {path}")
    total = counter.total(args.files)
    print(f"{total['lines']:>7} {total['words']:>7} {total['chars']:>8}  total")
    return 0
