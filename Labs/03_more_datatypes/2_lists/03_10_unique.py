'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list4 = input("insert a list of value: ")
list4 = list4.split()
#print(list4)

help_list = []
for i in list4:
    if list4.count(i) == 1:
        help_list.append(i)

print(help_list)

