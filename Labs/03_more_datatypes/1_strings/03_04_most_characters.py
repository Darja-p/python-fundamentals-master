'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
string1 = input("please input first string: ")
string2 = input("please input second string: ")
string3 = input("please input third string: ")

if len(string1) > len(string2) and len(string1) > len(string3):
    print(string1)
elif len(string2) > len(string1) and len(string2) > len(string3):
    print(string2)
else: print(string3)

