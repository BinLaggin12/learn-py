import random
from sys import excepthook

secret_number = random.randint(1,100)
attempts = 0
while True:
    try:
        guess = int(input("ENTER YOUR GUESS HERE:"))
        attempts += 1

        if guess < secret_number:
            print("aim higher!")
        elif guess > secret_number:
            print("aim lower!")
        else:
            print(f"CONGRATULATIONS!YOU HAVE WON THE GAME in {attempts} attempts! THE SECRET NUMBER WAS:  {secret_number}")
            break
    except ValueError:
        print("please enter a valid number!")




