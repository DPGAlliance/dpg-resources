"""Guard the platform-independence boundary: only the composition root and
adapters may reach beyond langchain-core."""

import ast
from pathlib import Path

SRC = Path(__file__).parents[1] / "src" / "pidemo"
VENDOR_PREFIXES = ("langchain_", "langsmith", "openai", "anthropic", "ollama")
ALLOWED = ("langchain_core",)
CORE = [SRC / "domain", SRC / "api.py", SRC / "config.py"]


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
    return names


def test_core_modules_import_no_vendor_packages():
    files = [f for p in CORE for f in ([p] if p.is_file() else p.rglob("*.py"))]
    assert files
    for f in files:
        for mod in imported_modules(f):
            if mod.startswith(ALLOWED):
                continue
            assert not mod.startswith(VENDOR_PREFIXES), f"{f.name} imports {mod}"
