import os
import re
import pickle
from collections import defaultdict


class Indexer:

    def __init__(self):
        self.index = defaultdict(list)
        self.documents = {}

    def index_directory(self, path):

        doc_id = 0

        for root, dirs, files in os.walk(path):

            for file in files:

                if file.endswith((".txt", ".md", ".html")):

                    filepath = os.path.join(root, file)

                    try:
                        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                            text = f.read()
                    except:
                        continue

                    self.documents[doc_id] = filepath

                    words = re.findall(r"\w+", text.lower())

                    for pos, word in enumerate(words):

                        self.index[word].append((doc_id, pos))

                    doc_id += 1

    def save(self, filename="index.pkl"):

        with open(filename, "wb") as f:
            pickle.dump((self.index, self.documents), f)

    def load(self, filename="index.pkl"):

        with open(filename, "rb") as f:
            self.index, self.documents = pickle.load(f)