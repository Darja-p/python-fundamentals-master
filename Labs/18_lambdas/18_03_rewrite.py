'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

print([x.startswith('D') for x in names])

print(list(filter(lambda name: name.startswith('D'), names)))


print(list(map(lambda s: s.startswith('D'),names)))
