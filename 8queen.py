def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col, n):
    if col == n:
        # All queens are placed successfully
        print_solution(board)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            if solve_queens(board, col + 1, n):
                return True

            # If placing queen in the current position doesn't lead to a solution,
            # backtrack and try placing the queen in a different row
            board[i][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))
    print("\n")

def solve_8_queens():
    n = 8
    board = [[0] * n for _ in range(n)]

    if not solve_queens(board, 0, n):
        print("Solution does not exist.")

if __name__ == "__main__":
    solve_8_queens()
