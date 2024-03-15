"""
    Prompt: Write a Python program that plays a simple game of Tic-Tac-Toe against the user. 
    The program should use a minimax algorithm to make its decisions.
"""

import copy

# Define the game state as a 3x3 grid of empty cells
game_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Define the player and computer symbols
player_symbol = "X"
computer_symbol = "O"

# Define the minimax algorithm's evaluation function
def evaluate_state(state):
    # Check if the game is won
    if (state[0][0] == state[0][1] == state[0][2] != 0) or \
       (state[1][0] == state[1][1] == state[1][2] != 0) or \
       (state[2][0] == state[2][1] == state[2][2] != 0) or \
       (state[0][0] == state[1][0] == state[2][0] != 0) or \
       (state[0][1] == state[1][1] == state[2][1] != 0) or \
       (state[0][2] == state[1][2] == state[2][2] != 0):
        # If the game is won, return the winner's score
        return 1 if state[0][0] == player_symbol else -1
    # If the game is a draw, return 0
    elif all(all(cell == 0 for cell in row) for row in state):
        return 0
    # Otherwise, return the maximum score of the next states
    else:
        next_states = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    new_state = copy.deepcopy(state)
                    new_state[i][j] = computer_symbol
                    next_states.append(new_state)
        return max([evaluate_state(next_state) for next_state in next_states])


# Define the game loop
while True:
    # Print the current game state
    print("Current state:")
    for row in game_state:
        print(" ".join(str(cell) for cell in row))
    print()

    # Ask the user for their move
    user_move = input("Enter row and column (e.g. 1 2): ")
    user_row, user_col = [int(x) for x in user_move.split()]

    # Make the user's move
    game_state[user_row][user_col] = player_symbol

    # If the game is won or drawn, print the result and exit
    if evaluate_state(game_state) != 0:
        print("Game over! You " +
              ("won" if evaluate_state(game_state) == 1 else "lost"))
        break

    # Make the computer's move using the minimax algorithm
    computer_move = None
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == 0:
                new_state = copy.deepcopy(game_state)
                new_state[i][j] = computer_symbol
                score = evaluate_state(new_state)
                if computer_move is None or score > evaluate_state(game_state):
                    computer_move = (i, j)

    # Make the computer's move
    game_state[computer_move[0]][computer_move[1]] = computer_symbol
