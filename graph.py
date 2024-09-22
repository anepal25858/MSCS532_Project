from collections import defaultdict

class Graph:
    def init(self):
        self.graph = defaultdict(list)

    def add_link(self, from_page, to_page):
        self.graph[from_page].append(to_page)

    def get_links(self, page):
        return self.graph[page]
