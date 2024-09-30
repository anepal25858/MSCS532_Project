# Updated invertedIndex.py
from collections import defaultdict
import pickle

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)
        self.cache = {}  # Adding cache for frequent searches

    def add_document(self, id, text):
        words = text.split()
        for word in words:
            word = word.lower()
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(id)

    def search(self, query):
        query = query.lower()
        if query in self.cache:
            return self.cache[query]

        result = self.index.get(query, [])
        if result:
            self.cache[query] = result
        return result

    # Lazy loading mechanism for large datasets
    def load_index_from_file(self, filepath):
        with open(filepath, 'rb') as f:
            self.index = pickle.load(f)

    def save_index_to_file(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self.index, f)
