from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming the graph is undirected

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # Perform BFS starting from vertex 2
    print("BFS starting from vertex 2:")
    g.bfs(2)
