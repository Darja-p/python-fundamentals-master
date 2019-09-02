'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

word = input("insert a name: ")
#sWord = slice(1, len(word), 1) this is slice constructor to slice object (start, stop, step)
#print(sWord)
print(str(word[slice(1, len(word), 1)]) + word[0] + "ay")
