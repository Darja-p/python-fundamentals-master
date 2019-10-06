'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
input_dict = {"item1": 5, "item2": 6, "item3": 1}

list1 = list(input_dict.items())
print(list1)

def takeSecond(elem):
    return elem[1]

sortedList = sorted(list1, key=takeSecond)
sortedList1 = sorted(list1, key=lambda elem: elem[-1])

print(sortedList)
print((sortedList1))