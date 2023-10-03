# 1. define a class Cat
# 2. define a constructor for each Cat object
    # 2.5. define Cat attributes as name, color, age
# 3. define properties for all Cat attributes
    # 3.5. how would you define these with the property function?
    # 3.5. how would you define these with decorators?
# 4. define methods for each Cat object
    # 4.5. define Cat methods as meow(), have_a_birthday()
# [OPTIONAL] 5. define overriding str magic method

class Cat():

    # constructor
    def __init__(self, name, color, age):
        self._name = name
        self._color = color
        self._age = age

    # make name property with property function
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    # make color property with decorators
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    # make age property with decorators
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    # instance methods
    def meow(self):
        print("Meeeeeeoooooooowwwwww!")

    def have_a_birthday(self):
        print("Happy birthday!")
        self.age = self.age + 1
        print(self.age)

    # str magic method
    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nAge: {self.age}"

# objects (instances of a class)
spice = Cat("Spice", "orange", 2)
cinnamon = Cat("Cinnamon", "brown", 4)
rufus = Cat("Rufus", "black", 2)

print(rufus)
print()
print(spice)
print()
print(cinnamon)