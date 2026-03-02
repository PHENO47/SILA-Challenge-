import numpy as np
import time
from datasets import load_dataset
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)
from utils import evaluate_model
import os

os.makedirs("data", exist_ok=True)

dataset = load_dataset("imdb")

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("label", "labels")
dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

train_dataset = dataset["train"].shuffle(seed=42).select(range(5000))
test_dataset = dataset["test"].shuffle(seed=42).select(range(2000))

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

training_args = TrainingArguments(
    output_dir="./data/bert_results",
    num_train_epochs=2,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    evaluation_strategy="epoch",
    save_strategy="no",
    logging_dir="./data/logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

start_train = time.time()
trainer.train()
end_train = time.time()

train_time = end_train - start_train

predictions = trainer.predict(test_dataset)
preds = np.argmax(predictions.predictions, axis=-1)

bert_metrics = evaluate_model(predictions.label_ids, preds)

print("DistilBERT:", bert_metrics)
print("Training time:", train_time)

trainer.save_model("data/bert_model")
tokenizer.save_pretrained("data/bert_model")

transformer_results = {
    "DistilBERT": bert_metrics,
    "BERT_train_time": train_time
}