from invertedIndex import InvertedIndex
from trie import Trie
from heap import Heap

# Test cases for inverted index
def testInvertedIndex():
    index = InvertedIndex()
    index.add_document(1, "machine learning algorithms")
    index.add_document(2, "deep learning")
    assert index.query("machine") == [1], "Test Failed"
    assert index.query("learning") == [1, 2], "Test Failed"
    print("Inverted Index Test Passed!")

# Test cases for trie auto-completion
def testTrie():
    trie = Trie()
    trie.insert("machine")
    trie.insert("learning")
    trie.insert("search")
    assert trie.search("ma") == ['machine'], "Test Failed"
    assert trie.search("le") == ['learning'], "Test Failed"
    print("Trie Test Passed!")

# Test cases for heap ranking
def testHeap():
    heap = Heap(k=3)
    heap.addPage(0.9, 1)
    heap.addPage(0.85, 2)
    heap.addPage(0.95, 3)
    assert heap.topRanked() == [(0.95, 3), (0.9, 1), (0.85, 2)], "Test Failed"
    print("Heap Test Passed!")

if __name__ == "__main__":
    testInvertedIndex()
    testTrie()
    testHeap()
