'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''

list_to_see = []


class Movie():
    def __init__(self, title, year,seen=" hasn't watched"):
        self.title = title
        self.year = year
        self.seen = seen

    def __str__(self):
        return f"this is a movie called {self.title}, from {self.year}, which you {self.seen}"

    def watch(self):
        self.seen = "watched already"
        return f" you watched {self.title}"

    def watch_list(self):
        if self.seen == "watched already":
            print(f"you have seen this movie already")
        else:
            list_to_see.append(self.title)
        return list_to_see


class RomCom(Movie):
    pass


class ActionMovie(Movie):
    def __init__(self, title, year, pg=13):
        super().__init__(title, year)
        self.pg = pg

    def __str__(self):
        return f"{self.title} from the year {self.year} with the rating {self.pg} ,{self.seen}"

pretty = Movie("Pretty woman", 1990)
print(pretty)
pretty.watch_list()
print(list_to_see)

la = RomCom("Love Actually", 2003)
print(la)
la.watch()
print(la)

mm = ActionMovie("Mad Max", 2015)
print(mm)
print(mm.seen)
mm.watch_list()
print(list_to_see)