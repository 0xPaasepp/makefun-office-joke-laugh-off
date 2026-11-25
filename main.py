#!/usr/bin/env python3
"""Write the office joke line to the grader output file — same bytes every run."""
from pathlib import Path

LINE = 'My boss said we\'re a family, so I asked HR who gets custody of my weekends.'

TARGET = Path('/output/entry.txt')


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(LINE, encoding='utf-8')


if __name__ == '__main__':
    main()
