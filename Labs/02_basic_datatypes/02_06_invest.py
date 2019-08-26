'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# Calculation future value with simple annual interest FV = I * [1 + (R * T)]
i = int(input("Please enter the investment amount: "))
r = float(input("Please enter the rate in percentage: "))
t = int(input("Please enter number of years: "))

fv = i * (1 + (r/100 * t))

print ("if you invest ", i ,"for", t, "years with", "%.1f%%" % (r), "you will get", fv)
