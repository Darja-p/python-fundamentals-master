'''
Write a script that demonstrates a try/except/else.

'''

try:
    input_here = input("please enter a name: ")
    if not input_here.isalpha():   #to check if input is only numbers  - if input_here.isdigit():
        raise TypeError

except TypeError:
    print(" wrong input, should be a name ")
else:
    print("What a beautiful name! :)")
