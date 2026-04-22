import os
import json
import zstandard as zstd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# CONFIG
# =============================
AI_DIR = "../AI"
HUMAN_DIR = "../HUMAN"

# =============================
# COMPRESSOR
# =============================
compressor = zstd.ZstdCompressor(level=10)

def compress(text: str) -> bytes:
    return compressor.compress(text.encode("utf-8"))

def compression_ratio(text: str) -> float:
    original = len(text.encode("utf-8"))
    if original == 0:
        return 0
    return len(compress(text)) / original

def bits_per_char(text: str) -> float:
    original = len(text.encode("utf-8"))
    if original == 0:
        return 0
    return (len(compress(text)) * 8) / original

# =============================
# LOAD JSONL DATA (PER SAMPLE)
# =============================
def load_jsonl_folder(folder, label):
    samples = []

    if not os.path.exists(folder):
        print(f"ERROR: Folder '{folder}' does not exist")
        return samples

    for fname in os.listdir(folder):
        if not fname.endswith(".jsonl"):
            continue

        path = os.path.join(folder, fname)

        if not os.path.isfile(path):
            continue

        print(f"Loading {path}...")

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f):
                try:
                    obj = json.loads(line)

                    text = obj.get("text", "").strip()
                    if not text:
                        continue

                    samples.append({
                        "file": fname,
                        "label": label,
                        "text": text
                    })

                except Exception as e:
                    print(f"Skipping bad line {i} in {fname}: {e}")

    return samples

# =============================
# LOAD DATA
# =============================
ai_samples = load_jsonl_folder(AI_DIR, "AI")
human_samples = load_jsonl_folder(HUMAN_DIR, "HUMAN")

print(f"\nLoaded {len(ai_samples)} AI samples")
print(f"Loaded {len(human_samples)} HUMAN samples")

if len(ai_samples) == 0 or len(human_samples) == 0:
    print("ERROR: One of the datasets is empty. Check your paths or files.")
    exit(1)

# =============================
# FEATURE EXTRACTION
# =============================
def compute_metrics(samples):
    results = []

    for i, sample in enumerate(samples):
        text = sample["text"]

        try:
            results.append({
                "file": sample["file"],
                "label": sample["label"],
                "size_bytes": len(text.encode("utf-8")),
                "compression_ratio": compression_ratio(text),
                "bits_per_char": bits_per_char(text),
            })
        except Exception as e:
            print(f"Error processing sample {i}: {e}")

    return results

ai_results = compute_metrics(ai_samples)
human_results = compute_metrics(human_samples)

df = pd.DataFrame(ai_results + human_results)

# =============================
# SUMMARY
# =============================
def summarize(df, label):
    subset = df[df["label"] == label]

    if subset.empty:
        print(f"WARNING: No data for {label}")
        return {
            "label": label,
            "samples": 0,
            "mean_ratio": None,
            "std_ratio": None,
            "mean_bpc": None,
            "std_bpc": None,
            "mean_size": None,
        }

    return {
        "label": label,
        "samples": len(subset),
        "mean_ratio": subset["compression_ratio"].mean(),
        "std_ratio": subset["compression_ratio"].std(),
        "mean_bpc": subset["bits_per_char"].mean(),
        "std_bpc": subset["bits_per_char"].std(),
        "mean_size": subset["size_bytes"].mean(),
    }

summary = pd.DataFrame([
    summarize(df, "AI"),
    summarize(df, "HUMAN")
])

# =============================
# OUTPUT
# =============================
print("\n=== SAMPLE RESULTS (first 10) ===\n")
print(df.head(10).to_string(index=False))

print("\n=== SUMMARY ===\n")
print(summary.to_string(index=False))

# =============================
# LENGTH FILTERING
# =============================
print("\n=== LENGTH FILTERING ===")

df_filtered = df[(df["size_bytes"] > 4000) & (df["size_bytes"] < 6000)]

print("Original samples:", len(df))
print("Filtered samples:", len(df_filtered))

print("AI filtered:", len(df_filtered[df_filtered["label"] == "AI"]))
print("HUMAN filtered:", len(df_filtered[df_filtered["label"] == "HUMAN"]))

print("\n=== FILTERED SUMMARY ===\n")

filtered_summary = pd.DataFrame([
    summarize(df_filtered, "AI"),
    summarize(df_filtered, "HUMAN")
])

print(filtered_summary.to_string(index=False))

#PLot

print("\n=== PLOTTING DISTRIBUTIONS ===")

plt.figure()
df_filtered[df_filtered["label"] == "AI"]["compression_ratio"].hist(bins=50, alpha=0.5)
df_filtered[df_filtered["label"] == "HUMAN"]["compression_ratio"].hist(bins=50, alpha=0.5)

plt.legend(["AI", "HUMAN"])
plt.title("Compression Ratio Distribution (Filtered)")
plt.xlabel("Compression Ratio")
plt.ylabel("Frequency")
plt.savefig("compression_ratio.png")
plt.close()


plt.figure()
df_filtered[df_filtered["label"] == "AI"]["bits_per_char"].hist(bins=50, alpha=0.5)
df_filtered[df_filtered["label"] == "HUMAN"]["bits_per_char"].hist(bins=50, alpha=0.5)

plt.legend(["AI", "HUMAN"])
plt.title("Bits per Character Distribution (Filtered)")
plt.xlabel("Bits per Char")
plt.ylabel("Frequency")
plt.savefig("bits_per_char.png")
plt.close()

# =============================
# COMPARISON
# =============================
try:
    ai_mean = summary.loc[summary["label"] == "AI", "mean_ratio"].iloc[0]
    human_mean = summary.loc[summary["label"] == "HUMAN", "mean_ratio"].iloc[0]

    print("\n=== COMPARISON ===")
    print("Mean compression ratio difference (AI - HUMAN):", ai_mean - human_mean)

    ai_bpc = summary.loc[summary["label"] == "AI", "mean_bpc"].iloc[0]
    human_bpc = summary.loc[summary["label"] == "HUMAN", "mean_bpc"].iloc[0]

    print("Mean bits-per-char difference (AI - HUMAN):", ai_bpc - human_bpc)

except Exception as e:
    print("Comparison failed:", e)