import random

pcard1 = 0
pcard2 = 0
pcard3 = 0
dcard1 = 0
dcard2 = 0

pcard1 = random.randint(1,10)
pcard2 = random.randint(1,10)
ptotal = pcard1 + pcard2
dcard1 = random.randint(1,10)
dcard2 = random.randint(1,10)
dtotal = dcard1 + dcard2

print(f'Your cards [{pcard1}, {pcard2}] Total: {ptotal}')
print(f'Computer 1st Card: {dcard1}')

while True:
    pcard3 = random.randint(1, 10)
    redraw = input('Would you like to draw again? (Y/N): ').lower()
    if redraw == 'y':
        ptotal += pcard3
        print(f'Total: {ptotal}')
        if ptotal > 21:
            print('You lost.')
            exit()
    elif redraw == 'n':
        break

if ptotal > dtotal:
    print(f'You win! {ptotal} > {dtotal}')
    exit()
elif ptotal < dtotal:
    print(f'You lose. {ptotal} < {dtotal}')
    exit()
elif ptotal == dtotal:
    print(f'Tie! {ptotal} = {dtotal}')
    exit()