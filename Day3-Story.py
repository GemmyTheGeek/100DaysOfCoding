def start_game():
    print("Welcome to the Quest of the Lost Relic!")
    print("You are an adventurer seeking the lost relic hidden deep in the forest.")
    print("Your quest begins now!\n")
    first_choice()


def first_choice():
    print("You are at the entrance of a dark forest. There are two paths.")
    print("1. Take the left path, where the trees are dense and eerie.")
    print("2. Take the right path, where you hear distant sounds of water.")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        dense_forest_path()
    elif choice == "2":
        river_path()
    else:
        print("Invalid choice, please try again.\n")
        first_choice()


def dense_forest_path():
    print("\nYou chose the left path and walk into the dense forest.")
    print("As you move deeper, you encounter a wild bear!")
    print("1. Try to scare it away with loud noises.")
    print("2. Slowly back away and take a different route.")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        print("\nThe bear is startled and runs away. You move forward safely.")
        relic_cave()
    elif choice == "2":
        print("\nYou back away, but the bear follows you. You barely escape and return to the forest entrance.")
        first_choice()
    else:
        print("Invalid choice, please try again.\n")
        dense_forest_path()


def river_path():
    print("\nYou chose the right path and follow the sound of water.")
    print("You find a river with a narrow bridge.")
    print("1. Cross the bridge carefully.")
    print("2. Look for another way around.")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        print("\nYou cross the bridge safely and continue on the path.")
        relic_cave()
    elif choice == "2":
        print("\nWhile searching for another way, you get lost and end up back at the forest entrance.")
        first_choice()
    else:
        print("Invalid choice, please try again.\n")
        river_path()


def relic_cave():
    print("\nYou find a hidden cave at the end of the path. The relic must be inside!")
    print("Inside, you see two passageways.")
    print("1. Take the left passage, which is narrow and dark.")
    print("2. Take the right passage, which seems well-traveled.")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        print("\nYou take the narrow passage and find a room filled with treasures!")
        print("Congratulations! You have found the Lost Relic and completed the quest!")
    elif choice == "2":
        print("\nYou take the well-traveled passage but find yourself back at the entrance of the cave.")
        print("The quest is not over yet! Try again.")
        relic_cave()
    else:
        print("Invalid choice, please try again.\n")
        relic_cave()


# Start the game
start_game()
