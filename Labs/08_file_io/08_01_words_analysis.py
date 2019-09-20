'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
from itertools import count

list1 = []
with open("words.txt",'r') as fin:
    for w in fin.readlines():
        w = w.rstrip()
        list1.append(w)

    print(list1)


    print(f"shortest word is: {min((word for word in list1), key=len)}")
    print(f"longest word is: {max((word for word in list1), key=len)}")
count1 = 0
for i in list1:
    count1 += 1

print(count1)




