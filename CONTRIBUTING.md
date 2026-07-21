# Contributing Guide

Thank you for contributing to the ElderlyAI Companion project.

This document describes the project structure, dataset format, and Git workflow to ensure consistency across all modules.


# Repository Structure

```
ElderlyAI_Companion/
│
├── Conversation/
├── Medical/
├── Wellness/
├── RAG/
├── notebooks/
├── finetuning/
├── README.md
├── CONTRIBUTING.md
└── requirements.txt
```

Each module should contain:

* `README.md`
* Training dataset (`*_train.json`)
* Dataset statistics (`*_statistics.json`)
* Any supporting resources specific to the module

---

# Dataset Format

All instruction-tuning datasets must use the following JSON structure:

```json
{
    "instruction": "...",
    "input": "...",
    "response": "...",
    "category": "...",
    "source": "..."
}
```

### Required Fields

| Field       | Description                    |
| ----------- | ------------------------------ |
| instruction | Instruction given to the model |
| input       | User query or prompt           |
| response    | Expected assistant response    |
| category    | Dataset category               |
| source      | Original dataset source        |

Do not rename these fields.


# Dataset Requirements

Before submitting your dataset:

* Remove duplicate records.
* Remove empty inputs or responses.
* Standardize the JSON format.
* Preserve the original dataset source.
* Generate dataset statistics.
* Document preprocessing steps in your module README.


# Preprocessing Notebook

Each module should include a preprocessing notebook in the `notebooks/` directory.

Example:

* `conversation_preprocessing.ipynb`
* `medical_preprocessing.ipynb`
* `wellness_preprocessing.ipynb`
* `rag_preprocessing.ipynb`


# Branch Strategy

Do not work directly on `main`.

Create a branch for your assigned module.

Recommended branch names:

* `conversation`
* `medical`
* `wellness`
* `rag`

When your work is complete:

1. Commit your changes.
2. Push your branch.
3. Open a Pull Request into `main`.


# Commit Messages

Use descriptive commit messages.

Examples:

* `feat: add conversation dataset`
* `feat: preprocess medical dataset`
* `docs: update module README`
* `fix: remove duplicate records`


# Coding Standards

* Use UTF-8 encoding.
* Use descriptive variable names.
* Add comments where appropriate.
* Keep preprocessing code reproducible.


# Before Opening a Pull Request

Please verify that:

* Dataset follows the required JSON schema.
* README is included.
* Statistics file is included.
* No duplicate records remain.
* No empty records remain.
* Notebook runs successfully from start to finish.


# Questions

If you are unsure about preprocessing, dataset formatting, or integration, contact the repository maintainer before merging changes.
