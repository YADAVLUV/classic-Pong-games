# classic-Pong-games
Pong Game
Overview
This is a simple Pong game implemented in Python using the Turtle graphics library. The game features two paddles, a bouncing ball, a scoring system, and a central line for visual separation. The first player to reach a score of 10 wins the game.

Features
Two-player mode (left player uses "W" and "S" keys; right player uses the "Up" and "Down" arrow keys)
Scoring system that tracks points for each player
Randomized Y-axis direction for the ball upon reset
Center line for visual clarity
Winner announcement when a player reaches 10 points
Technologies Used
Python 3.x
Turtle graphics library
Installation
Ensure you have Python 3.x installed on your machine. You can download it from python.org.
Clone this repository to your local machine using the command:
bash
Copy code
git clone https://github.com/yourusername/pong-game.git
Navigate to the project directory:
bash
Copy code
cd pong-game
Usage
Run the game by executing:
bash
Copy code
python main.py
Control the left paddle using the W (up) and S (down) keys.
Control the right paddle using the Up and Down arrow keys.
The game ends when a player reaches a score of 10, displaying the winner.
Files Structure
bash
Copy code
pong-game/
├── ball.py          # Contains the ball class and functionality
├── centerline.py    # Contains the class to draw the center line
├── main.py          # Main game loop and execution
├── paddle.py        # Contains the paddle class and functionality
├── scoreboard.py     # Handles the scoring system and winner display
└── README.md        # Project documentation
