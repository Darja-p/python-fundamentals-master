'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open('words.txt','r') as fin:
    list1 = []
    for w in fin.readlines():
        w = w.rstrip()
        list1.append(w)

print(list1)

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return "\n ".join(temp_list)

with open ('words_reverse.txt', 'w') as fout:
    fout.write(reverse_list(list1))

