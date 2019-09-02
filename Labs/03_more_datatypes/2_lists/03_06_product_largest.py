'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
input_list = input("input 10 different numbers: " )
alist = input_list.split()
alist = [float(i) for i in alist]

print (max(alist))

alist.sort()  #another way of finding the largest number through sorting the list
print (alist)
print (alist[9]) #printing the last number in the already sorted list
#print (alist.pop()) #this is just a test
#print (alist)
x = 0
for i in alist:
    x += float(i)
print (x)
