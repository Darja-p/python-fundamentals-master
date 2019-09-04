'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

for i in range(100):
    mod = i % 2
    if mod > 0:
        print(str(i))
