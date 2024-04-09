class Puzzle:
    def __init__(self, description, code, solution, difficulty):
        self.description = description
        self.code = code
        self.solution = solution
        self.difficulty = difficulty

class PuzzleGenerator:
    def __init__(self):
        self.puzzles = []  # Stores puzzle objects

    def generate_output_puzzle(self, difficulty):
        # Logic to create an output prediction puzzle

    def generate_debugging_puzzle(self, difficulty):
        # Logic to create a code debugging puzzle
        

    def generate_output_puzzle(self, difficulty):
        if difficulty == "easy":
            # ... (Logic from previous example)
        else:
            # Implement logic for harder difficulties later
            pass  

def display_puzzle(puzzle):
    print(puzzle.description)
    print(puzzle.code)

def get_player_answer():
    return input("Your answer: ")

def check_answer(puzzle, answer):
    return answer == puzzle.solution

if __name__ == "__main__":
    generator = PuzzleGenerator()
    puzzle = generator.generate_output_puzzle("easy")

    display_puzzle(puzzle)
    player_answer = get_player_answer()

    if check_answer(puzzle, int(player_answer)):  # Convert input to integer
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was {puzzle.solution}") 
        
        
from flask import Flask, jsonify

# ... (Your Puzzle and PuzzleGenerator classes)

app = Flask(__name__)
generator = PuzzleGenerator()

@app.route('/get-puzzle', methods=['GET'])
def get_puzzle():
    puzzle = generator.get_random_puzzle()
    return jsonify({
        'description': puzzle.description,
        'code': puzzle.code,
        'puzzleType': puzzle.puzzle_type
    })

if __name__ == '__main__':
    app.run(debug=True)