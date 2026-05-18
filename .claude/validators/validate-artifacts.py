#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / '.claude' / 'contracts' / 'artifact-registry.yaml'


def main() -> int:
    text = REGISTRY.read_text(encoding='utf-8')
    paths = re.findall(r'path:\s+(.+)', text)
    missing_parent_dirs = []
    for rel in paths:
        artifact_path = ROOT / rel.strip()
        if not artifact_path.parent.exists():
            missing_parent_dirs.append(str(artifact_path.parent.relative_to(ROOT)))
    if missing_parent_dirs:
        print('Artifact parent directories missing:')
        for item in missing_parent_dirs:
            print('-', item)
        return 1
    print('Artifact registry validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
