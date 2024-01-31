def is_valid_assignment(adjacency_map, assignment, node, color):
    for neighbor in adjacency_map[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

def backtracking(adjacency_map, colors, assignment, node_order):
    if len(assignment) == len(adjacency_map):
        return assignment

    current_node = node_order.pop(0)

    for color in colors:
        if is_valid_assignment(adjacency_map, assignment, current_node, color):
            assignment[current_node] = color
            result = backtracking(adjacency_map, colors, assignment, node_order)
            if result is not None:
                return result
            assignment.pop(current_node)

    node_order.insert(0, current_node)
    return None

def map_coloring(adjacency_map, colors):
    node_order = list(adjacency_map.keys())
    assignment = backtracking(adjacency_map, colors, {}, node_order)
    return assignment

# Example usage:
if __name__ == "__main__":
    # Example map represented by an adjacency map
    adjacency_map = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW']
    }

    # List of available colors
    colors = ['Red', 'Green', 'Blue']

    # Solve the map coloring problem
    solution = map_coloring(adjacency_map, colors)

    if solution:
        print("Map Coloring Solution:")
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")
