## 🕹️ Rock-Paper-Scissors Game (Python)

This is a simple **command-line Rock-Paper-Scissors game** written in Python. The user plays against the computer in real-time. It features clean modular code using custom utility and display modules for better structure and readability.

---

## 🚀 Features

- Play against a computer that makes random choices.
- Input validation (supports: `rock`, `paper`, `scissors`, or `exit`).
- Clean display messages and real-time score tracking.
- Organized using modules (`main.py`, `logic.py`, `display.py`, `utils.py`).

---

## 🧱 Project Structure
rock-paper-scissors/

│

├── main.py # Main game loop and core logic

├── game/

│ ├── logic.py # Winner decision logic

│ └── utils.py # Input cleaning function

├── tools/

│ └── display.py # All print/display functions

└── README.md

---

## 🎮 How to Play

1. **Clone the repository**:
   
   git clone https://github.com/yourusername/rock-paper-scissors.git
   cd rock-paper-scissors

2. **Run the game**:

python main.py

3. **Follow the prompts**:

Enter rock, paper, or scissors to play.

Type exit to quit the game.

---

## 📦 Dependencies

- Python 3.x
- No third-party libraries required (only random module from standard library)

## ⚙️ Upgrade ideas
We can upgrade it for more impact:

Add a GUI using Tkinter, PyGame, or Kivy

Add a score history using file I/O or database

Turn it into a web app using Flask

Add unit tests with pytest or unittest

Package it as a CLI tool using argparse
