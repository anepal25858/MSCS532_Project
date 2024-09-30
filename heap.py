class FibonacciHeapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.next = self
        self.prev = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key, value):
        node = FibonacciHeapNode(key, value)
        if self.min_node is None:
            self.min_node = node
        else:
            self._link_nodes(self.min_node, node)
        self.num_nodes += 1
        if node.key < self.min_node.key:
            self.min_node = node

    def _link_nodes(self, a, b):
        a.next.prev = b
        b.next = a.next
        a.next = b
        b.prev = a

    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                child = min_node.child
                while True:
                    next_child = child.next
                    self._link_nodes(min_node, child)
                    child.parent = None
                    child = next_child
                    if child == min_node.child:
                        break
            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev

            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
            self.num_nodes -= 1
        return min_node

    def is_empty(self):
        return self.min_node is None

    def get_min(self):
        return self.min_node


