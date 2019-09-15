'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    """ creating an object Car"""

    def __init__(self, model, year, max_speed=0):
        """defining main attributes of the class Car"""
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        """printing the details of the car"""
        return (f" model of the car - {self.model:^25}"
                f"\n year of production - {self.year:^20}"
                f"\n maximum speed is  - {self.max_speed:^20}")


    def accelerate(self):
        """defining method to increase speed by 5"""
        self.max_speed += 5



    def details(self):
        """defining method to print details of the car"""
        return print(f"{self.model} is {2019-self.year} years old and goes maximum {self.max_speed} ")


my_car = Car("Volvo", 2001, 65)
my_car.accelerate()
my_car.accelerate()

print(my_car.max_speed)
print(my_car)

my_car2 = Car("Skoda", 1995, 75)
my_car2.accelerate()
print(my_car2.max_speed)

my_car2.details()