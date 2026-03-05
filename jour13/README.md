# 🔎 Regex Search Engine with Inverted Index

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-green)
![Regex](https://img.shields.io/badge/Regex-Advanced-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **command-line full-text search engine** built with Python.

This project demonstrates how a search engine works internally using:

* **Recursive file indexing**
* **Inverted index**
* **Advanced Regex search**
* **TF-IDF ranking**
* **Result highlighting**
* **Index persistence using Pickle**

The tool scans text documents, builds an index, and allows powerful searches using **advanced regular expressions (PCRE-like patterns)**.

---

# 🚀 Features

✔ Recursive document indexing
✔ Inverted index (word → file + position)
✔ Advanced Regex search
✔ Result highlighting in terminal
✔ TF-IDF ranking (simplified)
✔ Snippet preview of results
✔ CLI interface
✔ Persistent index using **pickle**

---

# 🧠 How It Works

The search engine works in three main stages:

### 1️⃣ Indexing

The program scans a directory recursively and builds an **inverted index**.

Example structure:

```
python → [(doc1, 5), (doc2, 18)]
data → [(doc2, 7)]
```

Each word is mapped to the documents and positions where it appears.

---

### 2️⃣ Search

The user provides a **regular expression pattern**.

The engine scans indexed documents and returns matches.

Example:

```
python
python(?=.*data)
(?P<lang>python|java|rust)
```

---

### 3️⃣ Ranking

Results are ranked using a **simplified TF-IDF score**:

```
score = TF × IDF
```

Where:

* **TF** = term frequency in a document
* **IDF** = inverse document frequency

Documents with more relevant matches appear **first**.

---

# 📁 Project Structure

```
regex-search-engine/
│
├── main.py
├── indexer.py
├── searcher.py
├── utils.py
│
├── data/
│   └── example.txt
│
├── index.pkl
└── requirements.txt
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/regex-search-engine.git
```

Go into the project folder:

```bash
cd regex-search-engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the program:

```bash
python main.py
```

You will see the CLI menu:

```
1. Indexer un dossier
2. Rechercher
3. Quitter
```

---

# 📦 Step 1 — Index Documents

Choose option **1** and provide a folder containing text files.

Example:

```
Chemin du dossier : data
```

The program will scan all files recursively and build the index.

---

# 🔎 Step 2 — Search

Choose option **2** and enter a Regex pattern.

Example searches:

### Simple search

```
python
```

### Regex lookahead

```
python(?=.*data)
```

### Named group

```
(?P<language>python|java|rust)
```

---

# 📄 Example Output

```
🔎 2 result(s) found

📄 data/doc1.txt
Score TF-IDF: 1.27
... Python is widely used in data science ...

📄 data/doc2.txt
Score TF-IDF: 0.92
... learning python for machine learning ...
```

Matches are **highlighted in the terminal**.

---

# 🛠 Technologies Used

* Python
* `re` (Regular Expressions)
* `os`
* `pickle`
* Object-Oriented Programming (OOP)

---

# 🎯 Learning Goals

This project demonstrates concepts used in real search engines:

* Inverted indexing
* Text search algorithms
* Regular expression engines
* Information retrieval ranking (TF-IDF)

---

# 👨‍💻 Author

**PHENO47**
Future Full-Stack Developer | Cybersecurity Enthusiast | AI & Data Science Learner

GitHub:
https://github.com/PHENO47

---

# 📜 License

This project is open-source and available under the **MIT License**.
