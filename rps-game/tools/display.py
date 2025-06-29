def welcome_message(name):
    print(f"Welcome, {name}!")
    print("Let's play Rock, Paper, Scissors.")
    print("(Type 'exit' to quit.)")

def goodbye_message():
    print("Thanks for playing!")

def invalid_input_message():
    print("Invalid input. Please enter 'rock', 'paper', 'scissors', or 'exit'.")

def computer_move_message(move):
    print(f"Computer chose: {move}")

def round_result_message(result):
    print(result)

def score_message(user_score, computer_score):
    print("Score:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")