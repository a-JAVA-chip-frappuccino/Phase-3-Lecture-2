class Pup():

    # constructor
    def __init__(self, name, wags_tail, is_good_boy = True):
        self._name = name
        self._wags_tail = wags_tail
        self.is_good_boy = is_good_boy # merely an attribute

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # if isinstance(name, str):
        if type(name) == str and len(name) > 3:
            self._name = name
        else:
            raise Exception("Name must be a string with more than 3 characters!") # fatal error

    def get_wags_tail(self):
        return self._wags_tail
    
    def set_wags_tail(self, wags_tail):
        # if wags_tail == True or wags_tail == False:
        if type(wags_tail) == bool:
            self._wags_tail = wags_tail
        else:
            raise Exception("Tail wagging can be a Boolean value only!")

    wags_tail = property(get_wags_tail, set_wags_tail)

    # instance method
    def summon_pup(self):
        print(f"Come here, {self.name}!")

    # str magic method
    def __str__(self):
        return f"Name: {self.name}"

herschel = Pup("Herschel", True) # uses default is_good_boy value
prenup = Pup("Prenup", True, False)
springfrost = Pup("Spring Frost", False, True)

print(prenup)
print()
print(herschel)
print()
print(springfrost)