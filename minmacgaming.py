import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print('------')

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def is_terminal(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def minimax(self, depth, maximizing_player):
        if self.is_winner('X'):
            return -1
        elif self.is_winner('O'):
            return 1
        elif self.is_full():
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = 'O'
                eval = self.minimax(depth + 1, False)
                self.board[i][j] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for i, j in self.get_empty_cells():
                self.board[i][j] = 'X'
                eval = self.minimax(depth + 1, True)
                self.board[i][j] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_val = -math.inf
        best_move = None

        for i, j in self.get_empty_cells():
            self.board[i][j] = 'O'
            move_val = self.minimax(0, False)
            self.board[i][j] = ' '

            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val

        return best_move

# Example usage:
if __name__ == "__main__":
    game = TicTacToe()

    while not game.is_terminal():
        game.print_board()

        player_move = tuple(map(int, input("Enter your move (row, column): ").split()))
        if game.board[player_move[0]][player_move[1]] == ' ':
            game.board[player_move[0]][player_move[1]] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        if game.is_terminal():
            break

        print("Computer's move:")
        computer_move = game.find_best_move()
        game.board[computer_move[0]][computer_move[1]] = 'O'

    game.print_board()

    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("Computer wins!")
    else:
        print("It's a tie!")
