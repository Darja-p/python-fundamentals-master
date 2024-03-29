'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
# random list
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

# take second element for sort - function
def takeSecond(elem):
    return elem[1]


# sort list with key
sortedList = sorted(unsorted_list, key=takeSecond)

# print list
print('Sorted list:', sortedList)

mytuple = ("fourth", 9)
print(takeSecond(mytuple))