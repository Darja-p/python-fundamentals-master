'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

#file_name = 'integers.txt'

try:
    with open("integers.txt","r") as fin:
        a = (fin.read())
        a = a.split()
        a = int(a[0])
except ValueError:
    print("this is not a integer")
except IOError as ioe:
    print(ioe)
else: print(f"this is your number multiplied by 10: {a * 10}")
