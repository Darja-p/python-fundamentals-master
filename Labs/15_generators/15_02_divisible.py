'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

list1 = [1, 1111, 3, 2222, 2, 24, 3333]

for g in list1:
    if g % 1111 == 0:
        print(g)