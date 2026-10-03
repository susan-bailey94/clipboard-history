"""Clipboard History — Keep a searchable local history of clipboard text and restore any entry."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='clipboard_history',
        description='Keep a searchable local history of clipboard text and restore any entry.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Clipboard History')
    print('A local clipboard stack that does not leave the machine.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
