'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''

class Furniture():
    """creating class furniture with three attributes and one optional attribute 'position' """

    def __init__(self, category, material, color):
        self.category = category
        self.material = material
        self.color = color
        self.position = "nowhere"

    def __str__(self):
        if self.position =="nowhere":
            return f"this is a {self.category} made from {self.material} and is {self.color}."
        else: return f"this is a {self.category} made from {self.material} and is {self.color} and is in a {self.position}."

    def __repr__(self):
        return f"Furniture {self.category}, {self.material}, {self.color}, {self.position}"

    def moving(self,position):
        self.position = position
        return f'{self.color} {self.category} was moved to {self.position}'

class Plants:

    def __init__(self,name,color='green', location='terrace'):
        self.name = name
        self.color = color
        self.location = location

    def __str__(self):
        return f"this is a {self.name} which is {self.color} and which is in a {self.location}."


    def moving (self, location):
        self.location = location

class Drinks:
    """defining class drinks which has three attributes
       category, temperature and alcohol """

    def __init__(self, name, temperature, alcohol=0):
        self.name = name
        self.temperature = temperature
        self.alcohol = int(alcohol)

    def __str__(self):
        return f"this is a {self.temperature} {self.name} and is {self.alcohol} percents alcohol"

    def __add__(self, other):
        name = f"{self.name} with " + other.name
        temperature = f"{self.temperature} " + other.temperature
        alcohol = self.alcohol + other.alcohol
        return Drinks(name,temperature,alcohol)




tb = Furniture('table', 'wood', 'black')
print(tb)

tb.moving('kitchen')
print(tb)
repr(tb)

pm = Plants('palm')
print(pm)
pm.moving("kitchen")
pm.color="red"
print(pm)

gn = Drinks('gin','cold', 24)
tn = Drinks('tonic','cold')


print(tn)
print(gn)
cocktail = tn + gn
print(cocktail)
wh = Drinks('whiskey',"cold", 38)
cocktail2 = gn + wh
print(cocktail2)


