def decide_winner(user_move, computer_move):
    if user_move == computer_move:
        return "It's a draw!"
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        return "You win!"
    else:
        return "You lose!"