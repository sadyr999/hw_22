print("TASK 1")
from datetime import date
class Contact:
    def __init__(self, id, first_name, last_name, birth_date, profession) -> None:
        self.ID = id
        self.first_name = first_name
        self.last_name = last_name
        self.b_date = birth_date
        self.profession = profession
    def get_information(self):
        print(f"ID - {self.ID} Full name - {self.first_name} {self.last_name} Birth Date - {self.b_date} Profession - {self.profession}")

c = Contact(id=1, first_name='John', last_name='Dow', birth_date=date(day=21, month=4, year=1996), profession='Python developer')
d = Contact(id=2, first_name='Nick', last_name='Jones', birth_date=date(day=11, month=3, year=1991), profession='JS developer')
c.get_information()
d.get_information()

print("TASK 2")
from math import pi


class Fauna:
  def init(self, type, age):
    self.type = type
    try:
        self.age = int(age)
    except
        self.age = "NULL"
    self.can_swim
    self.can_fly
    self.can_kill_for_food

  def area(self):
    pass

  def fact(self):
    return "I am two-dimentional shape."

  def __str(self):
    return self.name


class Bird(Fauna):

  def init(self, a1)->None:
    super().init('Square')
    self.a = a1

  def __area(self):
    return self.a**2

class Fish(Fauna):
    def can_swim(self):

class Mammal(Fauna):

class Predator():
    def Eat(self):
        pass
class Herbivore():
    def Eat(self):
        pass
class Penguin(Bird, Herbivore):

class Falcon(Bird, Predator):

class Trout(Fish, Predator):

class Whale(Fish, Herbivore):

# >>>p = Penguin(type='royal', age='1 year') >>>p.eat() I eat fish >>>p.can_swim() True >>>p.can_fly() I cannot fly
