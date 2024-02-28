"""
    Prompt: Write a Python program that plays a simple game of Tic-Tac-Toe against the user. 
    The program should use a minimax algorithm to make its decisions.
    
    AI model B response:
    
    This program defines a TicTacToeState class to represent the current state of the board, 
    and a minimax function to make decisions based on the current state. The minimax function 
    uses a depth-limited search to explore the game tree and find the best move. 
    The TicTacToeState class has methods to evaluate the current state, check if the game is over, 
    get a list of possible moves, and make a move on the board. The play_game function runs the game loop,
    prompting the user for input and making moves on the board.
    
    Note that this is a simple implementation of the minimax algorithm, and you may want to improve it by using alpha-beta pruning, 
    iterative deepening, or other optimizations. Additionally, the heuristic function used to evaluate the state of the board is very 
    simple and may not lead to the best decisions. You can experiment with different heuristics to improve the performance of the algorithm.
"""


import copy

def minimax(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or state.game_over():
        return state.evaluate()

    if maximizing_player:
        best_move = None
        max_value = -float('inf')
        for move in state.get_moves():
            new_state = state.make_move(move)
            value = minimax(new_state, depth - 1, alpha, beta, False)
            if value > max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return best_move

    else:
        best_move = None
        min_value = float('inf')
        for move in state.get_moves():
            new_state = state.make_move(move)
            value = minimax(new_state, depth - 1, alpha, beta, True)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move

class TicTacToeState:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def evaluate(self):
        # Heuristic function to evaluate the current state
        # of the board. This is a simple implementation
        # that just counts the number of X's and O's on the board
        # and returns the difference.
        x_count = 0
        o_count = 0
        for row in self.board:
            for cell in row:
                if cell == 'X':
                    x_count += 1
                elif cell == 'O':
                    o_count += 1
        return x_count - o_count

    def game_over(self):
        # Check if the game is over by checking for
        # a win or a draw.
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return True
        for col in zip(*self.board):
            if col[0] == col[1] == col[2]:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return not any(cell == ' ' for row in self.board for cell in row)

    def get_moves(self):
        # Get a list of possible moves that can be made
        # on the current board.
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    moves.append((row, col))
        return moves

    def make_move(self, move):
        # Make a move on the board and return a new
        # TicTacToeState object representing the new board.
        row, col = move
        new_board = copy.deepcopy(self.board)
        new_board[row][col] = 'X' if self.turn == 'X' else 'O'
        self.turn = 'O' if self.turn == 'X' else 'X'
        return TicTacToeState()

def play_game():
    state = TicTacToeState()
    while not state.game_over():
        print(state.board)
        user_move = input('Enter a move (row, col): ')
        user_move = [int(x) for x in user_move.split(',')]
        state.make_move(user_move)
        computer_move = minimax(state, 4, -float('inf'), float('inf'), True)
        state.make_move(computer_move)

play_game()

