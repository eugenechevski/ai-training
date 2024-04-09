import random


class Puzzle:
    def __init__(self, description, code, solution, difficulty, puzzle_type):
        self.description = description
        self.code = code
        self.solution = solution
        self.difficulty = difficulty
        self.puzzle_type = puzzle_type  # New attribute for puzzle type

    def check_answer(self, user_answer):
        if self.puzzle_type == "output":
            return user_answer == self.solution
        elif self.puzzle_type == "debugging":
            try:
                exec(user_answer)
                return True  # If code runs without errors, it's considered correct for now
            except:
                return False


class PuzzleGenerator:
    def __init__(self):
        self.puzzles = []

    def generate_output_puzzle(self, difficulty):
        if difficulty == "easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            code = f"result = {num1} * {num2}\nprint(result)"
            solution = num1 * num2
            description = "What will this code print?"
            return Puzzle(description, code, solution, difficulty, "output")

    def generate_debugging_puzzle(self, difficulty):
        if difficulty == "easy":
            # Deliberate error: 'prnt' instead of 'print'
            code = "prnt('Hello, World!')"
            solution = "print('Hello, World!')"
            description = "Fix the error in this code:"
            return Puzzle(description, code, solution, difficulty, "debugging")

    def get_random_puzzle(self):
        # For simplicity, generate one of each type and choose randomly
        self.puzzles.append(self.generate_output_puzzle("easy"))
        self.puzzles.append(self.generate_debugging_puzzle("easy"))
        return random.choice(self.puzzles)


def play_game():
    generator = PuzzleGenerator()
    puzzle = generator.get_random_puzzle()

    print(puzzle.description)
    print(puzzle.code)

    user_answer = input("Your answer: ")
    if puzzle.check_answer(user_answer):
        print("Correct!")
    else:
        print("Incorrect. The correct solution is:")
        if puzzle.puzzle_type == "output":
            print(puzzle.solution)
        elif puzzle.puzzle_type == "debugging":
            print(puzzle.solution)


play_game()


