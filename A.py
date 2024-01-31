import heapq

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
        self.parent = None  # Add the parent attribute

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def astar(graph, start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_node.position)

        for neighbor in graph[current_node.position]:
            if neighbor not in closed_set:
                cost = current_node.cost + graph[current_node.position][neighbor]
                heuristic_value = heuristic(neighbor, goal)
                neighbor_node = Node(neighbor, cost, heuristic_value)
                neighbor_node.parent = current_node  # Set the parent

                if neighbor_node not in open_set:
                    heapq.heappush(open_set, neighbor_node)

    return None  # No path found

def heuristic(a, b):
    # Example Euclidean distance heuristic
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.position)
        node = node.parent
    return path

# Example usage:
if __name__ == "__main__":
    # Create a sample graph (weighted undirected graph)
    graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 1, (0, 2): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1, (2, 1): 1, (1, 2): 1},
        (0, 2): {(0, 1): 1, (1, 2): 1},
        (2, 0): {(1, 0): 1, (2, 1): 1},
        (2, 1): {(1, 1): 1, (2, 0): 1, (2, 2): 1},
        (1, 2): {(1, 1): 1, (0, 2): 1, (2, 2): 1},
        (2, 2): {(1, 2): 1, (2, 1): 1}
    }

    start = (0, 0)
    goal = (2, 2)

    path = astar(graph, start, goal)

    if path:
        print(f"Shortest path from {start} to {goal}: {path}")
    else:
        print("No path found.")
