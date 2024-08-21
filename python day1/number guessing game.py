#NUMBER GUESSING GAME
print("GREETINGS! WELCOME TO THE GAME. YOU HAVE 3 TRIES TO GUESS THE NUMBER BETWEEN 1-10. ARE YOU READY?")

#generate a random number between 1 and 10

import random
secret_number = random.randint(1,10)
max_attempts = 3
attempts = 0
#game loop
while attempts < max_attempts:
    guess = int(input("type your guess here:"))
    attempts += 1
    if guess == secret_number:
        print("congratulations! you won the game!")
        break
    elif guess > secret_number:
        print("you have to guess lower than that!")
    elif guess < secret_number:
        print('you have to guess higher than that!')
if attempts == max_attempts:

        print("the number was " + str(secret_number))


