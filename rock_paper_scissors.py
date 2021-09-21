import random

def play():
    print("Welcome to Rock Paper Scissors\n=================================")
    play_game = input("Would you like to play? y/n: ")   
    
    while play_game == 'y':
          
        user = input("Make your choice: 'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return "It's a tie"
        elif is_win(user, computer):
            return "Congratulations, you win!"

        return "You lost :("

    
    if play_game == 'n':
        print("Have a nice day!")
        exit 

# r > s, s > p, p > r

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or\
              (player == 'p' and opponent == 'r'):
        return True
    

print(play())
