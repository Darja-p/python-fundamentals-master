'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
inp = input("insert a number: ")
inp = int(inp)
def func1(a):
    if a % 4 == 0:
        return True
    elif a % 7 == 0:
        return True
    else:
        return False


print(f"NUmber is divisible by 4 or 7: {func1(inp)}")

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

def func2(a1):
    if a1 % 4 == 0:
        if a1 % 7 == 0:
            b1 = True
        else: b1 = False
    else: b1 = False
    return b1

print(f"Number is divisible by both 4 and 7: {func2(inp)}")


# take in a number from the user between 1 and 1,000,000,000



# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
