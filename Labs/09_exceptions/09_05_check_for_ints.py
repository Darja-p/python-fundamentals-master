'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

b=True
while b:
    i = input("Please insert a integer: ")
    try:
        i = int(i)
    except ValueError as e:
        print("This is not a integer")
    else:
        print("great! this is an integer")
        b=False
    #finally:
        #pass


