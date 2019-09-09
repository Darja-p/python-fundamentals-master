'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''
from typing import List

numbers_l = input("please insert numbers: ")
numbers_l = numbers_l.split()

print(numbers_l)
numbers_l.sort()
print(numbers_l)

len1 = len(numbers_l)
b = len1 % 2
print(b)
if b != 0:
    numbers_l.append(0)
print(numbers_l)

list1 = []
i = 0
while i < len1:
    list1.append(tuple(numbers_l[i:i+2]))
    i += 2
print(list1)
# another way to do with for using range with a step
for i in range(0,len1,2):
    list1.append(tuple(numbers_l[i:i+2]))
print(list1)


