from flask import Flask, request, jsonify
import torch
import joblib
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from utils import vader_predict

app = Flask(__name__)

# Load models
nb_model = joblib.load("data/naive_bayes_model.pkl")
bert_model = DistilBertForSequenceClassification.from_pretrained("data/bert_model")
tokenizer = DistilBertTokenizerFast.from_pretrained("data/bert_model")

bert_model.eval()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]
    model_type = data.get("model", "bert")

    if model_type == "vader":
        pred = vader_predict(text)
    elif model_type == "naive_bayes":
        pred = nb_model.predict([text])[0]
    else:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = bert_model(**inputs)
        pred = torch.argmax(outputs.logits).item()

    label = "positive" if pred == 1 else "negative"

    return jsonify({
        "model": model_type,
        "sentiment": label
    })

if __name__ == "__main__":
    app.run(debug=True)
{
  "text": "This movie is absolutely fantastic!",
  "model": "bert"
}