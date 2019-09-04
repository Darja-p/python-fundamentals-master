'''
Take two numbers from the user, an upper and lower bound.
Using a loop, calculate the sum of all numbers from the lower bound to the upper bound.

For example, if a user enters 1 and 100, the output should be:

The sum is: 5050
'''
upper, lower = input("Please insert two numbers - upper and lower bounds: ").split()
upper = int(upper)
lower = int(lower)
a = 0
for i in range (lower, upper + 1): #adding +1 to include upper number of the range in the calculation
    a += i
print(a)