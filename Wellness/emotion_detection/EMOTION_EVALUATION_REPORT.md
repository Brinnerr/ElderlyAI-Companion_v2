# Emotion Evaluation Report (v2 — Combined Dataset)
**Team:** Emotion Detection (Member 3 — CHEBOI)
**Date:** 2026-07-21
**Model:** distilbert-base-uncased, fine-tuned for 5-class emotion classification

## 1. Datasets used
- **GoEmotions** (Reddit comments, 27 emotions + neutral) — trained on.
  Link: https://huggingface.co/datasets/google-research-datasets/go_emotions
- **dair-ai/emotion** (Twitter messages, 6 emotions) — trained on.
  Link: https://huggingface.co/datasets/dair-ai/emotion
- **DAIC-WOZ** (clinical interviews) — NOT trained on; access-restricted (requires signed
  Data Use Agreement from USC ICT: https://dcapswoz.ict.usc.edu/). Documented here as a
  known limitation, to be integrated later once access is granted.

## 2. Label mapping
Both datasets were independently mapped onto the same 5 target classes: Happy, Sad, Angry, Fear, Neutral.
- GoEmotions: 27 fine-grained categories + neutral grouped into the 5 classes; conflicting
  multi-label rows dropped.
- dair-ai/emotion: joy/love -> Happy, sadness -> Sad, anger -> Angry, fear -> Fear, surprise -> Neutral.

## 3. Data sizes
- GoEmotions balanced train: 17654
- dair-ai/emotion balanced train: 8986
- Combined balanced train: 26640
- Combined validation: 6999
- Combined test: 7037

## 4. Version comparison
| Metric | v1 (GoEmotions only) | v2 (Combined) |
|---|---|---|
| Accuracy | 0.7217 | 0.7762 |
| Macro F1 | 0.6633 | 0.7704 |
| Macro Precision | 0.6316 | 0.7517 |
| Macro Recall | 0.7188 | 0.8021 |

Combining a second, stylistically different dataset (Twitter vs Reddit) improved every
metric, most notably Sad (F1 0.56 -> 0.81) and Fear (F1 0.64 -> 0.80).

## 5. Per-class performance (v2, combined model)

| class   |   precision |   recall |       f1 |   support |
|:--------|------------:|---------:|---------:|----------:|
| Happy   |    0.881716 | 0.839529 | 0.860106 |      2717 |
| Sad     |    0.787419 | 0.840278 | 0.81299  |       864 |
| Angry   |    0.574868 | 0.806758 | 0.671353 |       947 |
| Fear    |    0.739612 | 0.878289 | 0.803008 |       304 |
| Neutral |    0.774755 | 0.645805 | 0.704427 |      2205 |

## 6. Performance by data source (v2, combined model, evaluated on combined test set)

| source       |   accuracy |   f1_macro |    n |
|:-------------|-----------:|-----------:|-----:|
| dair_emotion |   0.9355   |   0.878954 | 2000 |
| go_emotions  |   0.712924 |   0.66132  | 5037 |

The model performs substantially better on Twitter-style text (dair-ai/emotion) than on
Reddit-style text (GoEmotions), suggesting Reddit comments are inherently harder to classify
(longer, more nuanced/sarcastic) than short, directly emotional social media posts.

## 7. Confusion matrix
See `reports/confusion_matrix_combined.png`. Main remaining weak point: true Neutral text is
sometimes misclassified as Angry (17% of Neutral test examples).

## 8. Known limitations
- DAIC-WOZ still not integrated into training (access-restricted); currently unlabeled
  spot-check only, described in Section 5 of the notebook.
- Angry has the lowest precision (0.57) of all classes — the model over-predicts Angry,
  especially on Neutral-leaning text.
- Reddit-style text remains harder than Twitter-style text for this model.

## 9. Deliverables produced
- `emotion_model_combined/` — final trained model + tokenizer (recommended for production use)
- `emotion_model/` — earlier v1 model (GoEmotions only), kept for comparison
- `emotion_api.py` — FastAPI service, now pointing at the combined model
- `reports/classification_report_combined.txt`, `reports/confusion_matrix_combined.png`
- `EMOTION_EVALUATION_REPORT.md` — this report
- `datasets/goemotions/`, `datasets/dair_emotion/`, `datasets/combined/` — all processed data, kept separately per source plus a combined version
