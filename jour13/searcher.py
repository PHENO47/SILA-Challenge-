import re
import math


class Searcher:

    def __init__(self, index, documents):

        self.index = index
        self.documents = documents

    def tf(self, term, doc_id):

        return len([x for x in self.index.get(term, []) if x[0] == doc_id])

    def idf(self, term):

        N = len(self.documents)

        docs_with_term = len(set(doc for doc, _ in self.index.get(term, [])))

        if docs_with_term == 0:
            return 0

        return math.log(N / docs_with_term)

    def tfidf(self, term, doc_id):

        return self.tf(term, doc_id) * self.idf(term)

    def search(self, pattern):

        regex = re.compile(pattern, re.IGNORECASE)

        results = []

        for doc_id, path in self.documents.items():

            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            except:
                continue

            matches = list(regex.finditer(text))

            if matches:

                score = 0

                words = re.findall(r"\w+", pattern.lower())

                for w in words:

                    score += self.tfidf(w, doc_id)

                results.append((score, path, matches, text))

        results.sort(key=lambda x: x[0], reverse=True)

        return results