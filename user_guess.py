import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, thats too low. Guess again!")
        elif guess > random_number: 
            print("Sorry, thats too high. Guess again!")

    print(f"Nice! {random_number} is the correct number!")
    
print(guess(10))
