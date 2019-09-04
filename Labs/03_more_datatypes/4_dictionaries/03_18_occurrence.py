'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

input1 = input("enter a string: ")
s = list(input1)
l = len(input1)
dict = {}
i = 0
while i < l:
    b = input1[i]
    dict[b] = input1.count(b)
    i = i +1
print(dict)
