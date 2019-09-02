'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
input1 = input("plese write a string: ").lower()
vowels = "aeiou"
a = 0
#for v in vowels: # this is a way to calculate how much each vowel appears in the sentence
    #print(v, input1.count(v))
for v in vowels:
    a += input1.count(v)
print(a)
