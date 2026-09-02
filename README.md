# AIDetx2-Dataset

Dataset created for the **AIDetx2** project.

The AIDetx2 dataset contains human-written and AI-generated text samples collected and generated for research on **AI-generated text detection** and **LLM model attribution**. The dataset includes human-written texts from multiple sources and AI-generated texts produced using several large language models (LLMs).

The dataset is intended to support research and evaluation of machine learning methods for distinguishing human-written text from AI-generated text and identifying the LLM responsible for generating a given text.

## Dataset Statistics

The dataset contains **923,162 text samples**, comprising human-written and AI-generated texts.

| Category  | Number of Samples |        Size |
| --------- | ----------------: | ----------: |
| Human     |           557,735 |     2.44 GB |
| AI        |           365,427 |     2.39 GB |
| **Total** |       **923,162** | **4.83 GB** |

### AI Samples by Model

AI-generated samples were produced using the following large language models:

| Model        | Number of Samples | Proportion |
| ------------ | ----------------: | ---------: |
| DeepSeek     |           102,875 |   28.15%   |
| GPT-OSS      |            69,988 |   19.15%   |
| LLaMA        |            61,460 |   16.82%   |
| Mistral 7B   |            75,351 |   20.62%   |
| Mistral Nemo |            55,753 |   15.26%   |
| **Total**    |      **365,427**  |  **100%**  |

## Human-Written Data Sources

The human-written portion of the dataset was constructed using text from multiple sources, including:

* **BBC News Dataset** — obtained from Kaggle.
* **News Dataset** — obtained from Kaggle.
* **arXiv** — academic papers retrieved through the arXiv API.
* **Open Library** — books used as a source of human-written text, subject to the copyright/public-domain status of the individual works.

The licensing and copyright status of each source should be considered independently. The inclusion of a text in this dataset does not imply that all source material is released under a single dataset-wide license.

## AI-Generated Data

The AI-generated portion of the dataset was produced using multiple open or openly available large language models.

The models used include:

* **Meta Llama 3.1 8B Instruct**
* **Mistral Nemo Instruct 2407**
* **Mistral 7B Instruct v0.3**
* **OpenAI GPT-OSS 20B**
* **DeepSeek-R1-Distill-Qwen-14B**

The model weights are **not distributed as part of this dataset**. The dataset contains generated text produced using these models.

The respective model licenses should be consulted when using or redistributing the generated data:

| Model                        | Model License               |
| ---------------------------- | --------------------------- |
| Llama 3.1 8B Instruct        | Llama 3.1 Community License |
| Mistral Nemo Instruct 2407   | Apache 2.0                  |
| Mistral 7B Instruct v0.3     | Apache 2.0                  |
| GPT-OSS 20B                  | Apache 2.0                  |
| DeepSeek-R1-Distill-Qwen-14B | MIT                         |

> **Note on Llama 3.1 outputs:** The Llama 3.1 Community License requires
> a "Built with Llama" attribution notice on content built using Llama
> outputs, and restricts using those outputs to train or improve LLMs
> other than Llama itself. Users incorporating the LLaMA-generated
> portion of this dataset into downstream training pipelines should
> review the [Llama 3.1 Community License](https://www.llama.com/llama3_1/license/)
> to confirm their use case is compliant.

## Dataset Structure

The repository is organized into separate directories for human-written and AI-generated samples, together with supporting metrics and verification files.

```text
AIDetx2-Dataset/
├── AI/
├── HUMAN/
├── METRICS/
├── .gitattributes
├── .gitignore
├── README.md
├── hashes_list.md5
├── md5sum_windows.ps1
└── script.sh
```

### AI

Contains the AI-generated text samples organized according to the model that generated each sample.

### HUMAN

Contains the human-written text samples collected from the dataset sources described above.

### METRICS

Contains dataset-related metrics and supporting information used during dataset preparation and analysis and teh respective script to used to obtain those metrics.

## Document IDs

Each sample is associated with a **document ID (`doc_id`)** identifying the source document from which the sample originates. Multiple samples may share the same `doc_id` when they are derived from the same source document.

The document IDs are used to preserve the relationship between samples originating from the same document. During dataset splitting, samples with the same `doc_id` can be kept within the same partition, preventing samples from the same source document from being distributed across training and test sets.

This grouping helps reduce the risk of **data leakage** and provides a more reliable evaluation of model generalization to previously unseen documents.


## Data Integrity and MD5 Checksums

To ensure the integrity of the dataset files, a file named **`hashes_list.md5`** is provided.

This file contains the MD5 checksum of each dataset file, allowing users to verify that the files have not been altered or corrupted.

### How to Verify

#### Ubuntu / Linux

Run the following command from the directory containing the dataset files and `hashes_list.md5`:

```bash
md5sum -c hashes_list.md5
```

Each file will be reported as `OK` if its checksum matches the expected value.

#### Windows

A PowerShell script named **`md5sum_windows.ps1`** is provided to perform the same verification.

Run the following command from the directory containing the dataset files and `hashes_list.md5`:

```powershell
.\md5sum_windows.ps1
```

If PowerShell prevents the script from running because of the execution policy, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

and then run the script again:

```powershell
.\md5sum_windows.ps1
```

## Licensing and Data Usage

The dataset contains material originating from multiple sources with potentially different licensing and copyright conditions. Consequently, **no single blanket license should be assumed to apply to all text contained in the dataset**.

The rights and licensing conditions of the original source material remain applicable to the corresponding data.

Users of the dataset are responsible for ensuring that their use of individual samples complies with the applicable source licenses and copyright restrictions.

The AI-generated samples were produced using models with the licenses identified above. The model weights and other model materials are not included in this dataset.

Where applicable, the dataset creators' contributions, including dataset organization, identifiers, annotations, and metadata, may be made available under terms specified in the corresponding dataset release.

For complete provenance and licensing information, users should consult the documentation accompanying each dataset release.

## Reproducibility

The repository provides supporting files intended to facilitate dataset verification and reproducible use, including:

* Document identifiers;
* MD5 checksums for dataset files;
* A Linux checksum verification procedure;
* A Windows PowerShell checksum verification script;
* Dataset metrics and supporting information.

When citing or using the dataset, users are encouraged to specify the dataset version or release used.

## Citation

If you use the AIDetx2 dataset in academic work, please cite the corresponding dataset release:

```bibtex
@dataset{aidetx2_dataset,
  author       = {Silva, Diogo},
  title        = {AIDetx2 Dataset},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {[VERSION]},
  doi          = {[DOI]}
}
```

A complete citation record will be provided once the dataset is published on Zenodo.

## Versioning

Dataset releases are versioned to ensure that published experiments remain reproducible.

When citing the dataset, use the DOI corresponding to the specific version used in your research whenever possible.

## Acknowledgements

This dataset was developed as part of the **AIDetx2** project and supports research into the detection and attribution of AI-generated text.

## Contact

For questions regarding the dataset, please use the issue tracker of the AIDetx2-Dataset repository or contact the dataset authors through the project repository.

---

**AIDetx2 Dataset — 2026**
