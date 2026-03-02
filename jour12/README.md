🧠 Advanced NLP Sentiment Analysis – Baseline vs Transformer
🚀 Project Overview

This project implements a bi-level sentiment analysis system using Python:

Baseline Model

VADER (NLTK)

TF-IDF Vectorization

Naive Bayes Classifier

Advanced Model

Fine-tuned DistilBERT (Hugging Face Transformers)

We compare both approaches on the IMDB movie reviews dataset, evaluate their performance, visualize sentiment distributions, and deploy a mini Flask API for real-time predictions.

🏗 Project Structure
sentiment-analyzer/
│
├── data/
│   └── imdb_sample.csv
│
├── baseline_model.py
├── transformer_model.py
├── compare_models.py
├── app.py
├── utils.py
├── requirements.txt
├── README.md
└── models/
📚 Technologies Used

Python 3.10+

nltk

scikit-learn

transformers

datasets

torch

flask

matplotlib

seaborn

pandas

📥 Dataset

We use the public IMDB dataset available via:

from datasets import load_dataset
dataset = load_dataset("imdb")

Binary sentiment classification:

0 → Negative

1 → Positive

🥇 1️⃣ Baseline Model
Architecture:

VADER sentiment analyzer

TF-IDF vectorization

Multinomial Naive Bayes classifier

Run:
python baseline_model.py
Output:

Accuracy score

Classification report

Confusion matrix

🤖 2️⃣ Transformer Model (DistilBERT)
Model:

distilbert-base-uncased

Fine-tuned using Hugging Face Trainer API.

Run:
python transformer_model.py
Output:

Accuracy

F1-score

Evaluation metrics

Saved model inside /models

📊 3️⃣ Model Comparison

To compare both models:

python compare_models.py

This script:

Displays accuracy comparison

Generates performance plots

Visualizes sentiment distribution

🌐 4️⃣ Flask API (Real-time Testing)

Launch the API:

python app.py

Then open:

http://127.0.0.1:5000

Send POST request:

{
  "text": "This movie was absolutely amazing!"
}

Response:

{
  "sentiment": "positive"
}
🖥 Installation (PC Version)
1️⃣ Clone repository
git clone https://github.com/PHEBO47/jour12.git
cd 
2️⃣ Create virtual environment
python -m venv venv

Activate:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
📈 Example Results (Typical)
Model	Accuracy
Baseline (NB)	~0.83
DistilBERT	~0.92+

Transformer clearly outperforms classical ML approach.

🔬 Evaluation Metrics

Accuracy

Precision

Recall

F1-score

Confusion Matrix

Sentiment Distribution Visualization

🏆 Challenge Requirements Validation

✅ Baseline with VADER + TF-IDF + Naive Bayes
✅ Fine-tuned Transformer (DistilBERT)
✅ Comparison on IMDB dataset
✅ Performance visualization
✅ Flask API deployment
✅ Clean project structure

📌 Future Improvements

Hyperparameter tuning

Cross-validation

Model quantization

Docker containerization

Streamlit web interface

Deploy on Render / Railway

👨‍💻 Author

PHENO47
Future Full-Stack Developer | Cybersecurity Enthusiast | AI Learner

⭐ If you like this project

Give it a ⭐ on GitHub!
