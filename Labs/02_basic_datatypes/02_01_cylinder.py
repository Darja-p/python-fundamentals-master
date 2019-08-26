'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

r = 3.14
h = 5
pi = 3.14
Volume = pi * r ** 2 * h
print ("Volume of a cylinder is ", Volume)

SurfArea = 2 * pi * r ** 2 + 2 * pi * r * h
print("Surface area is ", SurfArea)

pr = round(Volume,2) # testing how to round number
print (pr) # testing how to round number
