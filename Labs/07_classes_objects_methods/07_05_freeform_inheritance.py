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



class Movie():

    list_to_see = []

    def __init__(self, title, year, seen='have not seen'):
        """title should be a string"""
        self.title = title
        self.year = year
        assert (type(self.year) == int), "year must be an integer"
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
            Movie.list_to_see.append(self.title)
        return Movie.list_to_see


class RomCom(Movie):
    pass

class newRomCom(RomCom):
    """class for Rom Com movies from the last two years"""
    pass

class ActionMovie(Movie):

    def __init__(self, title, year, seen, pg =13):
        print(f"this is a pg {pg}")
        self.pg = pg
        super().__init__(title,year,seen)

    def __str__(self):
        return f"{self.title} from the year {self.year} with the rating {self.pg} which you {self.seen}"

pretty = Movie("Pretty woman", 1990)
print(pretty)
pretty.watch_list()
print(Movie.list_to_see)

la = RomCom("Love Actually", 1995)
print(la)
la.watch()
print(la)

ist = newRomCom("Isn't it romantic", 2019)
print(ist)
ist.watch()
ist.watch_list()

mm = ActionMovie("Mad Max", 2015,"not seen")
print(mm)
mm.watch_list()
print(Movie.list_to_see)