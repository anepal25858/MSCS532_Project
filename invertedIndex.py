from collections import defaultdict

class InvertedIndex:
    def __init__(self):

        self.index = defaultdict(list)

    def add_document(self, id, text):
        words = text.split()
        for word in words:
            self.index[word].append(id)

    def query(self, word):
        return self.index.get(word, [])
