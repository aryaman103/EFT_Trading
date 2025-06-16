# backend/sentiment.py
from transformers import pipeline
import numpy as np

# DistilBERT sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def score_sentiment(text: str) -> float:
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    score = result["score"]
    return score if label == "POSITIVE" else -score

def gpt_summary(texts: list[str]) -> str:
    # Stub for offline mode
    return " ".join(texts[:3])[:256]  # Truncate for demo 