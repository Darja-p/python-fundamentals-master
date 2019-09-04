'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

keys = range(10)
dict = {}
for i in keys:  #populating a dictionary using a for loop
    dict[i] = i*i
print(dict)