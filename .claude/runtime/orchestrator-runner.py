#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / '.claude' / 'settings.json'
STATE = ROOT / '.claude' / 'runtime' / 'project-state.yaml'
OUT = ROOT / 'output' / 'docs'


def main() -> int:
    settings = json.loads(SETTINGS.read_text(encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    print('Framework:', settings['frameworkName'])
    print('Orchestrator:', settings['orchestrator'])
    print('Output root:', settings['outputRoot'])
    print('State file:', STATE.relative_to(ROOT))
    print('Phases:')
    for phase in settings.get('phaseOrder', []):
        print('-', phase)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
