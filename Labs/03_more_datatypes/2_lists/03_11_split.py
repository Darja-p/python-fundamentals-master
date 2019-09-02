'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string_user = input("enter a string: ")
string_user = string_user.split()
list5 = [] #creating of an empty list
for i in string_user: #adding to the list count of each element
    sub = i
    list5.append(string_user.count(sub))

#print(list5)

for i in string_user: #comparing count of each item with the max count from list5 above
    if int(string_user.count(i)) == max(list5) :
        print(i)
        break


