import random

# List of words for the game
word_list = ["python", "hangman", "programming", "game", "gemmy"]

# Hangman stages in ASCII art
hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

def choose_word():
    return random.choice(word_list)

def play_hangman():
    word = choose_word()
    word_display = ["_"] * len(word)
    attempts = 0
    guessed_letters = []

    print("Welcome to Hangman!")
    while attempts < len(hangman_stages) - 1:
        print(hangman_stages[attempts])
        print("Word: " + " ".join(word_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    word_display[idx] = guess
            if "_" not in word_display:
                print("Congratulations, you've guessed the word!")
                print("Word:", word)
                break
        else:
            attempts += 1
            print("Incorrect guess. You have", len(hangman_stages) - 1 - attempts, "attempts left.")

    if attempts == len(hangman_stages) - 1:
        print(hangman_stages[attempts])
        print("Sorry, you've been hanged! The word was:", word)

play_hangman()
