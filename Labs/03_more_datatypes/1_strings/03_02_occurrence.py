'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
string_1 = input("insert a string: ")
letter= input("input a letter: ")
print(string_1.index(letter))
