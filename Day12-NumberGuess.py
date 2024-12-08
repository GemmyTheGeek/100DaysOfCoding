import random

gen_num = random.randint(0,100)
lives = 10

while not lives == 0:
    guess = int(input('Please enter a number between 0 - 100: '))
    if guess == gen_num:
        print('You won!')
        exit()
    elif guess < gen_num:
        print('Too less!')
        lives -= 1
        print(f'You have {lives} left')
    elif guess > gen_num:
        print('Too much!')
        lives -= 1
        print(f'You have {lives} left')

print('You lost!')
print(f'The number was {gen_num}')