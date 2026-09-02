#!/usr/bin/env python3
"""
count_samples.py — Count the number of JSON records in each NDJSON file in a directory.

Usage:
    python count_samples.py --input-dir ./my_jsons
    python count_samples.py --input-dir ./my_jsons --pattern "*.json"
"""

import argparse
import glob
import json
import os
import sys
from pathlib import Path


def human_size(num_bytes: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.2f} TB"


def count_samples(input_dir: str, pattern: str = "*.jsonl") -> None:
    search = os.path.join(input_dir, "**", pattern)
    files = sorted(glob.glob(search, recursive=True))

    if not files:
        print(f"[ERROR] No files matching '{pattern}' found in: {input_dir}")
        sys.exit(1)

    print(f"Found {len(files)} file(s) in '{input_dir}'\n")
    print(f"{'File':<50} {'Size':>10} {'Records':>10} {'Errors':>8}")
    print("-" * 82)

    total_records = 0
    total_errors  = 0

    for filepath in files:
        file_size    = os.path.getsize(filepath)
        record_count = 0
        error_count  = 0

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    json.loads(line)
                    record_count += 1
                except json.JSONDecodeError:
                    error_count += 1

        total_records += record_count
        total_errors  += error_count

        print(f"{Path(filepath).name:<50} {human_size(file_size):>10} {record_count:>10,} {error_count:>8,}")

    print("-" * 82)
    print(f"{'TOTAL':<50} {'':>10} {total_records:>10,} {total_errors:>8,}")


def main():
    parser = argparse.ArgumentParser(
        description="Count JSON records per NDJSON file in a directory."
    )
    parser.add_argument("--input-dir", "-i", required=True)
    parser.add_argument("--pattern",   "-p", default="*.jsonl")
    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"[ERROR] Directory not found: {args.input_dir}")
        sys.exit(1)

    count_samples(args.input_dir, args.pattern)


if __name__ == "__main__":
    main()