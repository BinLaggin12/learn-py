print("WELCOME! to the car game. please type help to get started!")
user_command = ""
started = False
while True:
    user_command = str(input("> ")).upper()
    if user_command == 'START':
        if started:
            print("car is already started!")
        else:
            started = True
            print("your car has started")
    elif user_command == 'STOP':
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print('your car has stopped')
    elif user_command == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit the game")
    elif user_command == "QUIT":
        print("you have quit the game, come back soon!")
        break
    else :
        print("i didn't quite catch that...")
