'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def firstF(parameter1):
    c = (f"this is what firstF does with {parameter1}")
    return c

def secondF(f):
    print(f)
    print(f)
    return f[0:5]

def thirdF(parameter3):
    b = secondF(parameter3) #when this function goes through this line it executes secondF (prints twice) and only then allocates return of secondF to variable b
    return firstF(b) #here function runs firstF with return of secondF and returns iy's result which is c

a = "Test parameter"
print(thirdF(a))


