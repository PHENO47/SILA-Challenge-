import random

class WordLoader:

    def __init__(self, filename="words.txt"):
        with open(filename, "r", encoding="utf-8") as f:
            self.words = [line.strip() for line in f if line.strip()]

        random.shuffle(self.words)
        self.index = 0

    def get_word(self):

        if self.index >= len(self.words):
            random.shuffle(self.words)
            self.index = 0

        word = self.words[self.index]
        self.index += 1

        return word