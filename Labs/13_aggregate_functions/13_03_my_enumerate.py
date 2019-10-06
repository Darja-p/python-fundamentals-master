'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(sequence, start=0):
    n = start
    result = []
    for elem in sequence:
        # yield n, elem
        result.append((n,elem))
        n += 1
    return result

print(list(my_enumerate([1,3,5,6])))

