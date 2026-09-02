import json
import re
import sys

def count_words(text: str) -> int:
    # Matches: contractions (don't), decimals (3.14), plain words, integers
    return len(re.findall(r"\b[a-zA-Z]+(?:'\w+)*\b|\b\d+(?:\.\d+)?\b", text))


def analyze_jsonl(file_path):
    word_counts = []
    count = 0
    lines_100 = []

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                print(f"Skipping invalid JSON on line {i}")
                continue

            text = obj.get("text", "")
            if not isinstance(text, str):
                text = str(text)

            wc = count_words(text)
            if wc <= 100:
                count += 1
                lines_100.append(i)
            word_counts.append(wc)

            print(f"Line {i}: {wc} words")

    if word_counts:
        print("\n--- Summary ---")
        print(f"Total entries: {len(word_counts)}")
        print(f"Min words: {min(word_counts)}")
        print(f"Max words: {max(word_counts)}")
        print(f"Avg words: {sum(word_counts) / len(word_counts):.2f}")
        print(f"Entries with <=100 words: {count}")
        print(f"Lines with <=100 words: {lines_100}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file.jsonl")
        sys.exit(1)

    analyze_jsonl(sys.argv[1])