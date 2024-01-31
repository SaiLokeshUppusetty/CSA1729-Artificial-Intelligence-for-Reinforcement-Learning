def is_valid(state):
    # Check if the state is valid (no missionaries eaten)
    left_bank = state[:3]
    right_bank = state[3:]

    if left_bank[0] < left_bank[1] or right_bank[0] < right_bank[1]:
        return False

    return True

def is_goal(state, goal):
    # Check if the current state is the goal state
    return state == goal

def generate_successors(state):
    # Generate possible successors from the current state
    successors = []

    for move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
        # Possible moves: (1, 0) or (0, 1) for moving 1 person, (2, 0) or (0, 2) for moving 2 people, (1, 1) for moving 1 missionary and 1 cannibal
        new_state = tuple(x + y if i < 3 else x - y for i, (x, y) in enumerate(zip(state, move)))

        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and 0 <= new_state[3] <= 3 and 0 <= new_state[4] <= 3 and is_valid(new_state):
            successors.append(new_state)

    return successors

def dfs_search(initial_state, goal_state):
    stack = [(initial_state, [])]

    while stack:
        current_state, path = stack.pop()

        if is_goal(current_state, goal_state):
            return path + [current_state]

        for successor in generate_successors(current_state):
            if successor not in path:
                stack.append((successor, path + [current_state]))

    return None

def print_solution(solution):
    # Print the solution path
    print("Missionaries and Cannibals Solution:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}: {state[:3]} | BOAT | {state[3:]}")

# Example usage:
if __name__ == "__main__":
    initial_state = (3, 3, 1, 0, 0)  # (missionaries on left, cannibals on left, boat on left, missionaries on right, cannibals on right)
    goal_state = (0, 0, 0, 3, 3)

    solution = dfs_search(initial_state, goal_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
