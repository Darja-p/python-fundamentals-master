'''
Print out every prime number between 1 and 100.

'''

for num in range (3,100):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)
