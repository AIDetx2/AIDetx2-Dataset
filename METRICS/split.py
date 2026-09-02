#!/usr/bin/env python3

import os
import argparse

BYTES_PER_GB = 1024 ** 3
DEFAULT_MAX_GB = 1.4


def human_size(num_bytes):
    for unit in ("B", "KB", "MB", "GB"):
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.2f} TB"


def split_jsonl(input_file, prefix, max_gb):
    max_bytes = int(max_gb * BYTES_PER_GB)

    part = 1
    current_size = 0
    out_f = None

    def new_file(p):
        filename = f"{prefix}_part{p}.jsonl"
        print(f"→ Creating {filename}")
        return open(filename, "w", encoding="utf-8")

    with open(input_file, "r", encoding="utf-8") as f:
        out_f = new_file(part)

        for line in f:
            encoded = line.encode("utf-8")
            size = len(encoded)

            if current_size + size > max_bytes:
                out_f.close()
                print(f"   Finished part {part} ({human_size(current_size)})")

                part += 1
                out_f = new_file(part)
                current_size = 0

            out_f.write(line)
            current_size += size

        if out_f:
            out_f.close()
            print(f"   Finished part {part} ({human_size(current_size)})")

    print("\nDone ✔")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output-prefix", default="human")
    parser.add_argument("-g", "--max-gb", type=float, default=DEFAULT_MAX_GB)

    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print("File not found")
        return

    split_jsonl(args.input, args.output_prefix, args.max_gb)


if __name__ == "__main__":
    main()