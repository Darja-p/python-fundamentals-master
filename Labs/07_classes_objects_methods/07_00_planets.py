'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''
class Planet():

  def __init__(self,name,color,galaxy):
    self.name = name
    self.color = color
    self.galaxy = galaxy


  def live(self):
    if self.name.lower() == 'earth':
      return f"yes, there is life on {self.name}"
    else: return f"looks like there is no life on {self.name}"

  def __str__(self):
    return f"the planet {self.name} is {self.color} and is in {self.galaxy}"


earth = Planet('Earth', 'blue','Milky Way' )
print(earth)
nept = Planet('Neptune', 'pale blue','Mily Way')
print(nept.live())
print(earth.live())