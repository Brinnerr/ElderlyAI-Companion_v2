# ElderlyAI Companion

## Overview

This repository contains the datasets, preprocessing pipelines, and fine-tuning resources for the ElderlyAI Companion project.

## Repository Structure

- Conversation/ – Conversational fine-tuning dataset
- Medical/ – Medical instruction dataset
- Wellness/ – Wellness and lifestyle dataset
- RAG/ – Retrieval-Augmented Generation resources
- notebooks/ – Dataset preprocessing notebooks
- finetuning/ – Fine-tuning scripts and checkpoints

## Team Workflow

- Conversation → Conversation branch
- Medical → Medical branch
- Wellness → Wellness branch
- RAG → RAG branch
- Emotion Classifier

All modules follow the same JSON schema:

```json
{
  "instruction": "...",
  "input": "...",
  "response": "...",
  "category": "...",
  "source": "..."
}
```