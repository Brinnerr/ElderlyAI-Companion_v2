
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_PATH = "./emotion_model_combined"   # trained on GoEmotions + dair-ai/emotion

app = FastAPI(title="Elderly Companion - Emotion Classification API")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

LABELS = [model.config.id2label[i] for i in range(len(model.config.id2label))]

class TextIn(BaseModel):
    text: str

class BatchIn(BaseModel):
    texts: list[str]

def _predict(texts):
    enc = tokenizer(texts, truncation=True, max_length=64, padding=True, return_tensors="pt")
    with torch.no_grad():
        logits = model(**enc).logits
    probs = torch.softmax(logits, dim=-1).tolist()
    out = []
    for p in probs:
        ranked = sorted(zip(LABELS, p), key=lambda x: -x[1])
        out.append({
            "emotion": ranked[0][0],
            "confidence": round(ranked[0][1], 4),
            "all_scores": {label: round(score, 4) for label, score in ranked},
        })
    return out

@app.get("/health")
def health():
    return {"status": "ok", "labels": LABELS}

@app.post("/predict")
def predict(payload: TextIn):
    return _predict([payload.text])[0]

@app.post("/predict_batch")
def predict_batch(payload: BatchIn):
    return _predict(payload.texts)
