type = input("What type of operation (/,x,-,+): ")
digit1 = float(input('What is the first digit: '))
digit2 = float(input('What is the second digit: '))

if type == "/":
    ans = digit1/digit2
    print(f'The answer is: {ans}')
elif type == "x":
    ans = digit1*digit2
    print(f'The answer is: {ans}')
elif type == "-":
    ans = digit1-digit2
    print(f'The answer is: {ans}')
elif type == "+":
    ans = digit1+digit2
    print(f'The answer is: {ans}')
else:
    print('Invalid Input. Please try again.')
    exit()
