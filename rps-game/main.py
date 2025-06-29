from game.utils import clean_input
from game.logic import decide_winner
import tools.display as dsp
import random

def main():
    user_name = input("Please enter your name: ")
    dsp.welcome_message(user_name)
    
    user_score = 0
    computer_score = 0
    print("hello")
    while True:
        user_move = input("Your move: ")
        cleaned_move = clean_input(user_move)
        
        if cleaned_move == "exit":
            dsp.goodbye_message()
            break
            
        if cleaned_move not in ["rock", "paper", "scissors"]:
            dsp.invalid_input_message()
            continue
            
        computer_move = random.choice(["rock", "paper", "scissors"])
        dsp.computer_move_message(computer_move)
        
        result = decide_winner(cleaned_move, computer_move)
        dsp.round_result_message(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
            
        dsp.score_message(user_score, computer_score)

if __name__ == "__main__":
    main()