import nltk
import numpy as np
import time
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def vader_predict(text):
    score = sia.polarity_scores(text)["compound"]
    return 1 if score >= 0 else 0

def evaluate_model(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary"
    )
    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

def measure_time(func):
    start = time.time()
    result = func()
    end = time.time()
    return result, end - start

def save_metrics(metrics_dict, path="data/metrics.json"):
    with open(path, "w") as f:
        json.dump(metrics_dict, f, indent=4)