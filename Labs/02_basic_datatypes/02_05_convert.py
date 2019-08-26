'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

a = 2
print (a)
a = float (a)
print(a)

b = 3.4  #the decimal part of the number will be lost
b = int (b)
print (b)

print (10 // 3) #the decimal part of the result will be lost
# just to test standard division print (10 / 3)

print (10 // 3.5) #the decimal part of the result will be lost
# just to test standard division print (10 / 3.5)

c ,d = input("Please insert two numbers: ").split()
c = float (c)
d = float (d)

print( c * d)

