import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j], 3)
                    heuristic += abs(i - goal_row) + abs(j - goal_col)
        return heuristic

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def get_neighbors(node):
    i, j = get_blank_position(node.state)
    neighbors = []

    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i, new_j = i + move[0], j + move[1]
        if is_valid_move(new_i, new_j):
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, move, node.cost + 1))

    return neighbors

def print_solution(node):
    path = []
    while node:
        path.append((node.action, node.state))
        node = node.parent
    path.reverse()
    for move, state in path:
        print("Move:", move)
        for row in state:
            print(row)
        print()

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    priority_queue = [initial_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            print("Solution found!")
            print_solution(current_node)
            return

        visited.add(tuple(map(tuple, current_node.state)))

        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor.state)) not in visited:
                heapq.heappush(priority_queue, neighbor)

    print("No solution found.")

# Example usage:
initial_puzzle = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
solve_8_puzzle(initial_puzzle)
