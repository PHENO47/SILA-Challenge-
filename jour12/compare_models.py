import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datasets import load_dataset
import os

os.makedirs("data/figures", exist_ok=True)

# Distribution dataset
dataset = load_dataset("imdb")
labels = dataset["train"]["label"]

plt.figure()
sns.countplot(x=labels)
plt.title("Distribution des Sentiments - IMDB")
plt.savefig("data/figures/distribution.png")

# Comparison table
results = pd.DataFrame({
    "Model": ["VADER", "Naive Bayes", "DistilBERT"],
    "Accuracy": [0.70, 0.85, 0.92],  # Replace with real metrics
})

print(results)

plt.figure()
sns.barplot(x="Model", y="Accuracy", data=results)
plt.title("Model Accuracy Comparison")
plt.ylim(0,1)
plt.savefig("data/figures/accuracy_comparison.png")