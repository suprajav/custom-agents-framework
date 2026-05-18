#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PHASE_MAP = ROOT / '.claude' / 'contracts' / 'phase-input-output-map.yaml'
EXPECTED = [
    'requirement',
    'design',
    'planner',
    'implementation',
    'testing',
    'quality',
    'compliance',
    'coverage_analyzer',
    'deployment',
]


def main() -> int:
    text = PHASE_MAP.read_text(encoding='utf-8')
    missing = [phase for phase in EXPECTED if ('  {}:'.format(phase) not in text)]
    if missing:
        print('Missing phase contract entries:')
        for item in missing:
            print('-', item)
        return 1
    print('Phase handoff validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
