# AIDetx2-Dataset

Dataset created for the **AIDetx2** project.

## MD5 Checksum Verification

To ensure the integrity of the dataset files, a file named **`hashes_list.md5`** is provided.

This file contains the MD5 checksum of each dataset file, allowing you to verify that the files have not been altered or corrupted.

### How to Verify

#### Ubuntu / Linux

Run the following command from the directory containing the dataset files and `hashes_list.md5`:

```bash
md5sum -c hashes_list.md5
```

Each file will be reported as `OK` if its checksum matches the expected value.

#### Windows

Run the provided **`md5sum_windows.ps1`** PowerShell script from the directory containing the dataset files and `hashes_list.md5`:

```powershell
.\md5sum_windows.ps1
```

If PowerShell prevents the script from running because of the execution policy, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

and then run the script again.

## Dataset Metrics

The dataset contains **860,987 text samples**, comprising both human-written and AI-generated texts. The AI-generated samples were produced using multiple large language models (LLMs).

| Category  |Number of Samples|   Size    |
| --------- | ---------------:|  ------:  |
| Human     |          557,735|  2.44GB   |
| AI        |          365,427|  2.39GB   |
| **Total** |      **923,162**| **4.83GB**|

### AI Samples by Model

| Model        | Number of Samples | Proportion  |
| ------------ | ----------------: | ----------: |
| DeepSeek     |           102,875 |    19.15%   |
| GPT-OSS      |            69,988 |    28.15%   |
| LLaMA        |            61,460 |    16.82%   |
| Mistral 7B   |            75,351 |    20.62%   |
| Mistral Nemo |            55,753 |    15.26%   |
| **Total AI** |       **367,012** |   **100%**  |
