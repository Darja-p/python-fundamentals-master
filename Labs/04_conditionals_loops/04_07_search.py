'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
a = int(input("input a number:"))
counter = 0
while counter <= 1000000000:
    if counter == a:
        print(counter)
        break
    counter += 1

