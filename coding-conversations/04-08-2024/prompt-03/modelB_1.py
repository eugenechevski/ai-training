# Using Flask
from flask import Flask, jsonify
from puzzle_generator import PuzzleGenerator

app = Flask(__name__)
generator = PuzzleGenerator()

@app.route('/generate_puzzle')
def get_puzzle():
    puzzle = generator.get_random_puzzle()
    return jsonify(puzzle.__dict__)