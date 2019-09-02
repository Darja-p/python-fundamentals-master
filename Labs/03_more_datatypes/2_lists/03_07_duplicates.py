'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]
list_st_ = set(list_) #changing  list for set takes out all duplicates
print(list(list_st_))

list_ = [1, 2, 3, 4, 3, 4, 5]
list_.sort()
b = 0
c = len(list_)
while b < c-1:
    if list_[b]==list_[b+1]:
        del list_[b]
        c = c -1
    b += 1

print(list_)
