'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

try:
    c, d = input("Please insert two numbers: ").split()
    c = float(c)
    d = float(d)
    qot = c/d
except ZeroDivisionError:
    print ("you entered zero as second number and quotient can not be calculated")
except ValueError:
    print("error! please enter numbers")
else:
    print(qot)