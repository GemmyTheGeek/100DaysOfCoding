import random
import string


def generate_password():
    # Ask the user for the number of letters, symbols, and numbers
    num_letters = int(input("Enter the number of letters: "))
    num_symbols = int(input("Enter the number of symbols: "))
    num_numbers = int(input("Enter the number of numbers: "))

    # Define character sets
    letters = string.ascii_letters  # includes both uppercase and lowercase
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    numbers = string.digits

    # Generate random characters
    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

    # Combine all characters
    password_list = password_letters + password_symbols + password_numbers

    # Shuffle the list to make the password random
    random.shuffle(password_list)

    # Join the list into a single string
    password = ''.join(password_list)

    return password


# Generate the password
print("Your generated password is:", generate_password())
