income= int(input("enter you income"))
if income <= 20000:
    tax= 0.02*income
    print("your tax is",tax)
elif income <= 50000:
    tax= 400+.025*(income-20000)
    print("your tax is",tax)
else:
    tax = 1150+.035(income-50000)
    print ("your tax is",tax)

