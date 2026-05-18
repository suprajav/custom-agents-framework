#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / '.claude' / 'settings.json'
INPUT = ROOT / 'input'


def main() -> int:
    settings = json.loads(SETTINGS.read_text(encoding='utf-8'))
    missing = []
    for name in settings.get('requiredInputs', []):
        path = INPUT / name
        if not path.is_file():
            missing.append(str(path.relative_to(ROOT)))
    if missing:
        print('Missing required inputs:')
        for item in missing:
            print('-', item)
        return 1
    print('Input validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
