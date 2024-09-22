from invertedIndex import InvertedIndex
from trie import Trie
from heap import Heap

def main():
    index = InvertedIndex()
    trie = Trie()
    heap = Heap(k=3)

    index.add_document(1, "machine learning algorithms")
    index.add_document(2, "deep learning and artificial intelligence")
    index.add_document(3, "machine learning for search engines")
    trie.insert("machine")
    trie.insert("learning")
    trie.insert("search")

    print("Documents containing 'learning':", index.query("learning"))

    print("Auto-complete for 'ma':", trie.search("ma"))

    heap.addPage(0.9, 1)
    heap.addPage(0.85, 2)
    heap.addPage(0.95, 3)

    print("Top 3 relevant documents:", heap.topRanked())

if __name__ == "__main__":
    main()
