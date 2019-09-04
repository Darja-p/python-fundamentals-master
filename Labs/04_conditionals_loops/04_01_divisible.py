'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
number1 = int(input("please input a number between 1 and 1 000 000 000: "))
b = number1 % 3
if number1 > 1000000000:
    print("number is not correct")
else:
    if b == 0:
        print(str(number1) + " is divisible by 3")
    else: print("try again")
