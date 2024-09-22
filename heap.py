import heapq

class Heap:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def addPage(self, score, id):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, (score, id))
        else:
            heapq.heappushpop(self.heap, (score, id))

    def topRanked(self):
        return sorted(self.heap, reverse=True)
