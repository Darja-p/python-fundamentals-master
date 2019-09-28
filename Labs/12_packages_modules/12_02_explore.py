'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''

# importing built in module random
import random

# printing random integer between 0 and 5
print(random.randint(0, 5))
# printing floating number
print(random.random())

# importing built in module datetime


import time

# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())


import datetime

print("Current date and time: " , datetime.datetime.now())

now = datetime.datetime.now()
print(now.year)

#creating a tuple with the important date and time parameters
time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)

print(time_now)
