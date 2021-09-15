import random

def computer_guess(x):
    #you can change the range as you wish
    print("Think of a number between 1 and 10\n=================================")
    low = 1
    high = x
    feedback = ""
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct(C)? ").lower()
        if feedback == 'h': 
            high = guess -1
        elif feedback == 'l':
            low == guess + 1
    print(f"Well done computer! {guess} is the correct number")
#change argument for new range
computer_guess(10)
