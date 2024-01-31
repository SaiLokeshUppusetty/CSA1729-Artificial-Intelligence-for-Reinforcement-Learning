from collections import deque

def water_jug_problem(capacity_x, capacity_y, target):
    visited_states = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()

        if current_state[0] == target or current_state[1] == target:
            return reconstruct_path(current_state)

        visited_states.add(current_state)

        # Fill jug X
        fill_x = (capacity_x, current_state[1])
        if fill_x not in visited_states:
            queue.append(fill_x)

        # Fill jug Y
        fill_y = (current_state[0], capacity_y)
        if fill_y not in visited_states:
            queue.append(fill_y)

        # Empty jug X
        empty_x = (0, current_state[1])
        if empty_x not in visited_states:
            queue.append(empty_x)

        # Empty jug Y
        empty_y = (current_state[0], 0)
        if empty_y not in visited_states:
            queue.append(empty_y)

        # Pour water from jug X to jug Y
        pour_xy = (max(0, current_state[0] - (capacity_y - current_state[1])), min(capacity_y, current_state[1] + current_state[0]))
        if pour_xy not in visited_states:
            queue.append(pour_xy)

        # Pour water from jug Y to jug X
        pour_yx = (min(capacity_x, current_state[0] + current_state[1]), max(0, current_state[1] - (capacity_x - current_state[0])))
        if pour_yx not in visited_states:
            queue.append(pour_yx)

    return None

def reconstruct_path(final_state):
    path = [final_state]
    while final_state != (0, 0):
        if final_state[0] == 0:
            path.append((0, final_state[1]))
            final_state = (0, final_state[1])
        elif final_state[1] == 0:
            path.append((final_state[0], 0))
            final_state = (final_state[0], 0)
        elif final_state[0] > 0 and final_state[1] > 0:
            path.append((final_state[0], 0))
            final_state = (final_state[0], 0)
    return path[::-1]

# Example usage:
if __name__ == "__main__":
    capacity_x = 4
    capacity_y = 3
    target = 2

    solution_path = water_jug_problem(capacity_x, capacity_y, target)

    if solution_path:
        print("Water Jug Problem Solution:")
        for state in solution_path:
            print(f"Jug X: {state[0]}, Jug Y: {state[1]}")
    else:
        print("No solution found.")
