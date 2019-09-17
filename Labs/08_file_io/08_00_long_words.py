'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with open("words.txt","r") as fin:
    list1 = []


    for w in fin.readlines():
        w = w.rstrip()
        if len(w) > 20:
            list1.append(w)


    print(list1)
