# thawrefund4d-kit

Count lines, words and characters, with totals.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m thawrefund4d_kit.cli --help
```

```python
from thawrefund4d_kit.core import Thawrefund4dTool

tool = Thawrefund4dTool()
print(tool)
```

## Layout

```
thawrefund4d_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 thawrefund4d
