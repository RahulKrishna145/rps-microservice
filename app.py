from flask import Flask, jsonify
import random

app = Flask(__name__)

MOVES = ['rock', 'paper', 'scissors']

@app.route('/play/<user_move>')
def play(user_move):
    if user_move not in MOVES:
        return jsonify({"error": "Invalid move. Choose rock, paper, or scissors."}), 400
    
    computer_move = random.choice(MOVES)
    
    # Game Logic
    if user_move == computer_move:
        result = "It's a tie!"
    elif (user_move == 'rock' and computer_move == 'scissors') or \
         (user_move == 'paper' and computer_move == 'rock') or \
         (user_move == 'scissors' and computer_move == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({
        "user_move": user_move,
        "computer_move": computer_move,
        "result": result,
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
