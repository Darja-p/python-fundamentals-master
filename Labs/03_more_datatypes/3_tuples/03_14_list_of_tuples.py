'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

input_string = input("please input a string: ")
input_string = input_string.split()
print(input_string)

len1 = len(input_string) #to find how many words we have in a string - to use in a while below
l: int = 0

list1 = []  #defining a list in which we will collect tuples)
#list1.append(list(tuple(input_string[0])))
#list1 = (tuple(input_string[0]),tuple(input_string[1]))


while l < len1:
    list1.append(tuple(input_string[l]))
    l += 1

print(list1)



