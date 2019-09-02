'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
list2 = input("please enter 10 numbers: ")
list2 = list2.split()
list3 = (list2[1],list2[3],list2[5],list2[7],list2[9],list2[8],list2[6], list2[4], list2[2], list2[0])
print(list3)