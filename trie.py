# Updated trie.py
class CompressedTrieNode:
    def __init__(self, value=''):
        self.value = value
        self.children = {}
        self.is_end_of_word = False

class CompressedTrie:
    def __init__(self):
        self.root = CompressedTrieNode()

    def insert(self, word):
        node = self.root
        i = 0
        while i < len(word):
            for child_value, child_node in node.children.items():
                common_prefix = self._common_prefix(child_value, word[i:])
                if common_prefix:
                    # Split the node if partial match is found
                    if common_prefix != child_value:
                        self._split_node(node, child_value, common_prefix, child_node)
                    node = node.children[common_prefix]
                    i += len(common_prefix)
                    break
            else:
                # No common prefix found, create new child
                node.children[word[i:]] = CompressedTrieNode(word[i:])
                node = node.children[word[i:]]
                i = len(word)
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        i = 0
        while i < len(word):
            for child_value, child_node in node.children.items():
                if word[i:].startswith(child_value):
                    node = node.children[child_value]
                    i += len(child_value)
                    break
            else:
                return False
        return node.is_end_of_word

    def _common_prefix(self, s1, s2):
        common = ""
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                common += c1
            else:
                break
        return common

    def _split_node(self, parent, old_key, new_prefix, child):
        # Split the current node into two nodes for compression
        new_child = CompressedTrieNode(new_prefix)
        remaining = old_key[len(new_prefix):]
        new_child.children[remaining] = child
        parent.children[new_prefix] = new_child
        del parent.children[old_key]
