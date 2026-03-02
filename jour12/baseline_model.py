from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os
from utils import vader_predict, evaluate_model, measure_time

os.makedirs("data/figures", exist_ok=True)

dataset = load_dataset("imdb")

train_texts = dataset["train"]["text"][:10000]
train_labels = dataset["train"]["label"][:10000]
test_texts = dataset["test"]["text"][:2000]
test_labels = dataset["test"]["label"][:2000]

# ---------------- VADER ----------------
vader_preds = [vader_predict(t) for t in test_texts]
vader_metrics = evaluate_model(test_labels, vader_preds)
print("VADER:", vader_metrics)

# ---------------- TF-IDF + NB ----------------
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_features=10000)),
    ("clf", MultinomialNB())
])

_, train_time = measure_time(lambda: pipeline.fit(train_texts, train_labels))

nb_preds, infer_time = measure_time(lambda: pipeline.predict(test_texts))

nb_metrics = evaluate_model(test_labels, nb_preds)

print("Naive Bayes:", nb_metrics)
print("Training time:", train_time)
print("Inference time:", infer_time)

# Save model
joblib.dump(pipeline, "data/naive_bayes_model.pkl")

# Confusion Matrix
cm = confusion_matrix(test_labels, nb_preds)
plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix - Naive Bayes")
plt.savefig("data/figures/confusion_matrix_nb.png")

baseline_results = {
    "VADER": vader_metrics,
    "Naive_Bayes": nb_metrics,
    "NB_train_time": train_time,
    "NB_infer_time": infer_time
}