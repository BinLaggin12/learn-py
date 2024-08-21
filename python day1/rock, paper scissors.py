choice = ['rock', 'paper', 'scissors']
import random
print("welcome to the game, pick rock(R), paper(P) or scissors(S)!")
attempts = 0
for attempts in range (0,11):
    computer_choice = random.choice(choice)
    attempts += 1
    guess = str(input("please put your attempt here: ")).upper()
    if guess == 'R':
        if computer_choice == choice[2]:
            print('You won this round! I picked ' + str(computer_choice))
        elif  computer_choice == choice[1]:
            print('You lost this round! I picked ' + str(computer_choice))
        else:
            print('This round is a tie! I picked ' + str(computer_choice))
    elif guess == 'P':
        if computer_choice == choice[0]:
            print('You won this round! I picked ' + str(computer_choice))
        elif computer_choice == choice[2]:
            print('You lost this round! I picked ' + str(computer_choice))
        else:
            print('This round is a tie! I picked ' + str(computer_choice))
    elif guess == 'S':
        if computer_choice == choice[1]:
            print('You won this round! I picked ' + str(computer_choice))
        elif computer_choice == choice[0]:
            print('You lost this round! I picked ' + str(computer_choice))
        else:
            print('This round is a tie! I picked ' + str(computer_choice))
    else:
        print('invalid input. please choose R,P or S')







