import random
from os import system #for windows

def game():
    user = int(input('Choose 1 (Rock), 2 (Paper), 3 (Scissors): '))

    if user != 1 and user != 2 and user != 3:
        print('Invalid Number. Please try again.')
        exit()

    com = random.randint(1,3)

    if com == 1:
        print('Computer chooses Rock')
    elif com == 2:
        print('Computer chooses Paper')
    elif com == 3:
        print('Computer chooses Scissors')

    if user == 1 and com == 2:
        print("Computer wins!")
    elif user == 1 and com == 3:
        print('You win!')
    elif user == 2 and com == 3:
        print("Computer wins!")
    elif user == 2 and com == 1:
        print('You win!')
    elif user == 3 and com == 1:
        print("Computer wins!")
    elif user == 3 and com == 2:
        print('You win!')
    elif user == com:
        print("Draw!")

    again = input('Would you like to play again? (Y/N): ')
    if again.upper() == "Y":
        system('cls')
        game()
    if again.upper() == "N":
        exit()
    else:
        print("Invalid Input. Exiting Game.")
        exit()

game()