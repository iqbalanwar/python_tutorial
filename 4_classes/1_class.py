'''
When an object is created from a class, 'self' will reference
that object. Everything that is defined in the class is
dereferenced off itself to get the instantiated object version
of it (through the period '.' operator).
- self is a reference to the object (like 'this' in JS/Java)
- self is always used as the first parameter

Putting an underscore at the beginning of the variables discourages
users of the object to access the variables directly. That's why the
getters are there.
'''

class Animal:
    # This is a class variable, NOT an object variable
    # It's defined in the class, not in any method
    # x = [1, 2, 3]

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
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
    print_animal(Animal())

    '''
    PROBLEMATIC CODE:
    print(a0.x)
    a1.x[0] = 7
    print(a0.x)

    The reason this is problematic is because the class variable is 
    being modified. Since the variable is referenced in the class and
    not in a specific object, any modifications to that class variable
    is accessible in all objects of that class (any object).

    Note: DO NOT PUT MUTABLE DATA IN A CLASS. If you must but a constant
    inside a class, MAKE SURE IT IS IMMUTABLE

    That's why encapsulation is important. Since x is a class variable,
    it is accessible by all objects of that class and is therefore not
    encapsulated. However, the variables attached to the constructor are
    encapsulated, so they're attached to individual objects. Furthermore,
    don't directly set/get object variables; convention is to use the
    given setters/getters
    '''

if __name__ == '__main__': main()
