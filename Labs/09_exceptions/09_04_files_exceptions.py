'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

import os
path = os.environ.get('MY_PATH')
print(path)
cwd = os.getcwd()
print(cwd)




with open(f'/{path}/09_exceptions/books/war_and_peace.txt','r') as fin:
    wap = fin.read()
    x = len(list(wap))

with open(f'/{path}/09_exceptions/books/crime_and_punishment.txt','w') as fin1:
    fin1.write(' bla bla   ')


class MyException(Exception):
    def __init__(self, value):
        self.value = value
    pass

try:
    """with open(f'(/{path}/09_exceptions/books/war_and_peace.txt', 'r') as fin:
        wap1 = list(fin.read())"""
    wap1 = wap[0:100]
    with open(f'/{path}/09_exceptions/books/pride_and_prejudice.txt', 'r') as fin2:
        wap2 = list(fin2.read())
        wap2 = wap2[0:100]
    with open(f'/{path}/09_exceptions/books/crime_and_punishment copy.txt', 'r') as fin3:
        wap3 = list(fin3.read())
        wap3 = wap3[0:100]

    def prince(book):
        c = "".join(book).lower()
        d = c.count("prince")
        if d > 0:
            return True
        else: False


    if prince(wap1):
        raise MyException("War and peace")
    if prince(wap2):
        raise MyException("Pride and Prejudice")
    if prince(wap3):
        raise MyException("Crime and Punishment")

except MyException as error:
    print("Attenzione! There is a word 'Prince' in the first 100 characters of the book", error)

finally:
    try:
        ch = 1

        # Walking a directory tree and printing the names of the directories and files
        for dirpath, dirnames, files in os.walk(f'/{path}/09_exceptions/books'):
            print(f'Found directory: {dirpath}')
            for file_name in files:
                print(file_name)
                with open(dirpath+'/'+file_name, 'r') as fin2:
                    wap2 = list(fin2.read())
                    print(wap2[ch])

            """with open('/Users/daria/Documents/CodingNomads/Labs/09_exceptions/books/war_and_peace.txt', 'r') as fin:
                wap1 = list(fin.read())
            print(wap[ch])
            with open("/Users/daria/Documents/CodingNomads/Labs/09_exceptions/books/pride_and_prejudice.txt",'r') as fin2:
                wap2 = list(fin2.read())
                print(wap2[ch])
            with open("/Users/daria/Documents/CodingNomads/Labs/09_exceptions/books/crime_and_punishment.txt", 'r') as fin3:
                wap3 = list(fin3.read()) #this list has three items, so program ends. should we open a copy to use the whole file?
                print(wap3[ch])"""
            ch += 1

    except Exception as e:
        print(e)




