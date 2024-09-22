class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, W):
        node = self.root
        for c in W:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        return self.getWords(node, prefix)

    def getWords(self, node, prefix):
        w = []
        if node.is_end_of_word:
            w.append(prefix)
        for c, child in node.children.items():
            w.extend(self.getWords(child, prefix + c))
        return w
