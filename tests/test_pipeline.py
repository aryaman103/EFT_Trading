# tests/test_pipeline.py
from backend.sentiment import score_sentiment

def test_sentiment_range():
    pos = score_sentiment("This is great!")
    neg = score_sentiment("This is terrible.")
    assert -1.0 <= pos <= 1.0
    assert -1.0 <= neg <= 1.0 