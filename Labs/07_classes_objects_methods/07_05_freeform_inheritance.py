'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
list_to_see = []


class Movie():
    def __init__(self, title, year, seen='have not seen'):
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

class newRomCom(RomCom):
    """class for movies from the last two years"""


class ActionMovie(Movie):
    def __int__(self, title, year, seen, pg=13):  #parameter pg can't be added
        super().__int__(title, year, seen)
        self.pg = pg

    def __str__(self):
        return f"{self.title} from the year {self.year} with the rating {self.pg} which you {self.seen}"  #this is not working because pg is not created for actionmovie

pretty = Movie("Pretty woman", 1990)
print(pretty)
pretty.watch_list()
print(list_to_see)

la = RomCom("Love Actually", 2003)
print(la)
la.watch()
print(la)

ist = newRomCom("Isn't it romantic", 2019)
print(ist)
ist.watch()
ist.watch_list()

mm = ActionMovie("Mad Max", 2015)
#print(mm)
mm.watch_list()
print(list_to_see)