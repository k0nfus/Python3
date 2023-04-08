import random

random_number = random.randint(1,1000)
guess = None

while True:
    guess = input("Pick a number between 1 and 1000: ")
    guess = int(guess)
    if guess < random_number:
        print("too low!")
    elif guess > random_number:
        print("too high!")
    else:
        print("YOU WON!!!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1,1000)
            guess = None
        else:
            print("Thank you for playing!")
            break