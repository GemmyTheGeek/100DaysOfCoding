total = float(input("Total amount: "))
tip = int(input('How much do you want to tip (5, 10, 12, 15, 20): '))
if tip in (5,10,12,15,20):
    pass
else:
    print("This tip amount is invalid. Please try again")
    exit()
people = int(input('How many people will be splitting the bill: '))
allbill = total*((tip+100)/100)
indibill = allbill/people
print("Your total is $"+str(allbill)+"\nEach person should pay $"+str(indibill))