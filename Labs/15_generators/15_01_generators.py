'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

gen1 = (x for x in range(4))
print(gen1)

for i in gen1:
    print(i)