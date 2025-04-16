from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}  

    def add_edge(self, u, v):
        # Add edge u -> v
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
        
        # if v not in self.adj_list:
        #     self.adj_list[v] = []
        # self.adj_list[v].append(u)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()

        queue.append(start_vertex)
        visited.add(start_vertex)

        print("BFS traversal order:")

        while queue:
            current = queue.popleft()
            print(current, end=' ')

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

g.bfs(0)  



