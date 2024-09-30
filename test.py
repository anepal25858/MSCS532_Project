import tracemalloc
import timeit
from invertedIndex import InvertedIndex
from trie import CompressedTrie
from heap import FibonacciHeap

def test_inverted_index():
    print("Testing Inverted Index...")
    index = InvertedIndex()

    # Adding documents
    index.add_document(1, "machine learning algorithms")
    index.add_document(2, "deep learning and artificial intelligence")
    index.add_document(3, "machine learning applications in healthcare")

    # Test search functionality
    assert index.search("algorithms") == [1]
    assert index.search("learning") == [1, 2, 3]
    assert index.search("notfound") == []

    print("Inverted Index tests passed!")

def test_compressed_trie():
    print("Testing Compressed Trie...")
    trie = CompressedTrie()

    # Inserting words
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("helicopter")

    # Test search functionality
    assert trie.search("hello") == True
    assert trie.search("hell") == True
    assert trie.search("helicopter") == True
    assert trie.search("hi") == False

    print("Compressed Trie tests passed!")

def test_fibonacci_heap():
    print("Testing Fibonacci Heap...")
    heap = FibonacciHeap()
    heap.insert(5, "five")
    heap.insert(2, "two")
    heap.insert(8, "eight")

    min_node = heap.extract_min()
    assert min_node.key == 2

    heap.insert(1, "one")
    min_node = heap.extract_min()
    assert min_node.key == 1
    print("Fibonacci Heap tests passed!")

def performance_tests():
    print("Running performance tests...")

    index = InvertedIndex()
    large_document = "machine learning deep learning AI NLP algorithms" * 1000
    index.add_document(1, large_document)
    index.add_document(2, "search engine optimization algorithms")

    time_taken = timeit.timeit(lambda: index.search("algorithms"), number=1000)
    print(f"Inverted Index search took {time_taken:.6f} seconds")

    trie = CompressedTrie()
    for i in range(10000):
        trie.insert(f"test{i}")

    time_taken = timeit.timeit(lambda: trie.search("test9999"), number=1000)
    print(f"Compressed Trie search took {time_taken:.6f} seconds")

    heap = FibonacciHeap()
    for i in range(10000):
        heap.insert(i, f"value{i}")

    # Time extract_min
    time_taken = timeit.timeit(lambda: heap.extract_min(), number=1000)
    print(f"Fibonacci Heap extract_min took {time_taken:.6f} seconds")

if __name__ == "__main__":
    test_inverted_index()
    test_compressed_trie()
    test_fibonacci_heap()

    performance_tests()
