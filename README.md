# AIDetx2-Dataset
Dataset created for the AIDetx2


## MD5 Checksum Verification

To ensure the integrity of the dataset files, a file named **`hashes_list.md5`** is provided.  
This file contains the MD5 checksums for each dataset file, allowing you to verify that the files have not been altered or corrupted.

### How to verify

Run the following command in the directory containing your dataset files:

```bash
md5sum -c hashes_list.md5
```

## Dataset Metrics


To ensure 


Loaded 367012 AI samples
Loaded 493975 HUMAN samples

=== SAMPLE RESULTS (first 10) ===

                file label  size_bytes  compression_ratio  bits_per_char
mistral_7b_ids.jsonl    AI        4989           0.491682       3.933454
mistral_7b_ids.jsonl    AI        4038           0.439079       3.512630
mistral_7b_ids.jsonl    AI        5790           0.464767       3.718135
mistral_7b_ids.jsonl    AI        4937           0.382418       3.059348
mistral_7b_ids.jsonl    AI        6054           0.481830       3.854642
mistral_7b_ids.jsonl    AI        6410           0.418565       3.348518
mistral_7b_ids.jsonl    AI        4448           0.458633       3.669065
mistral_7b_ids.jsonl    AI        5414           0.481714       3.853713
mistral_7b_ids.jsonl    AI        5563           0.461262       3.690095
mistral_7b_ids.jsonl    AI        6653           0.436795       3.494363

=== SUMMARY ===

label  samples  mean_ratio  std_ratio  mean_bpc  std_bpc   mean_size
   AI   367012    0.465472   0.061200  3.723779 0.489599 6727.701666
HUMAN   493975    0.456579   0.063697  3.652629 0.509577 4715.893509

=== LENGTH FILTERING ===
Original samples: 860987
Filtered samples: 303153
AI filtered: 109446
HUMAN filtered: 193707

=== FILTERED SUMMARY ===

label  samples  mean_ratio  std_ratio  mean_bpc  std_bpc   mean_size
   AI   109446    0.467585   0.028537  3.740678 0.228296 5087.725189
HUMAN   193707    0.446169   0.044258  3.569351 0.354062 5520.730025

=== PLOTTING DISTRIBUTIONS ===

=== COMPARISON ===
Mean compression ratio difference (AI - HUMAN): 0.008893835100873326
Mean bits-per-char difference (AI - HUMAN): 0.07115068080698661
