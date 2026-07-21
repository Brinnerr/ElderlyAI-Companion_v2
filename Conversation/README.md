# Conversation Dataset

## Project
**Elderly AI Companion System**

## Module
Conversation & Empathy

## Overview
This dataset was prepared for supervised fine-tuning (SFT) of the conversational module of the Elderly AI Companion.

## Source Datasets
- EmpatheticDialogues
- PersonaChat
- DailyDialog

## Dataset Format
Each sample contains:
- instruction
- input
- response
- category
- source

## Preprocessing
- Unified all datasets into one JSON format.
- Removed duplicate input-response pairs.
- Removed empty records.
- Removed speaker labels from DailyDialog.
- Shuffled the final dataset.

## Files
- empathetic_train.json
- persona_train.json
- dailydialog_train.json
- conversation_train.json
- conversation_statistics.json
- README.md

## Intended Use
This dataset is intended for supervised fine-tuning of the conversational component of the Elderly AI Companion.
