'''
When an object is created from a class, 'self' will reference
that object. Everything that is defined in the class is
dereferenced off itself to get the instantiated object version
of it (through the period '.' operator).
- self is a reference to the object (like 'this' in JS/Java)
- self is always used as the first parameter

See the use of this in main(). Remember, quack() and move() are
objects.

Putting an underscore at the beginning of the variables discourages
users of the object to access the variables directly. That's why the
getters are there.
'''

class Animal:
    # standard constructor:
    # def __init__(self, type=None, name=None, sound=None):
    #     self._type = type
    #     self._name = name
    #     self._sound = sound

    # constructor with multiple keyword arguments
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'
    
    # Standard Getters:
    # def type(self): return self._type
    # def name(self): return self._name
    # def sound(self): return self._sound

    # The following three functions work as getters AND setters
    def type(self, t=None):
        if t: self._type = t
        return self._type
    def name(self, n=None):
        if n: self._name = n
        return self._name
    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():

    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rawr')
    a1 = Animal(type = 'puppy', name = 'pal', sound = 'woof')
    # object instantiation with standard constructor:
    # a1 = Animal('puppy', 'pal', 'woof')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type = 'velociraptor', name = 'veronica', sound = 'hello'))
    print_animal(Animal())

if __name__ == '__main__': main()
