'''
Inheritance is one of the core tenants of OOP
You need to know how constructors work in inheritance
'''

class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    def type(self, t=None):
        # This is a try catch block in python
        # This is the normal way to use a setter-getter
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n=None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s=None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

class Duck(Animal):
    def __init__(self, **kwargs):
        # Initializes the type for Duck
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)
    
    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')

# Class to reverse a string
# Inherits from standard string class built into python
class RevStr(str):
    def __str__(self):
        # returns slice of string, where step goes backwards
        return self[::-1]


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')


def main():
    a0 = Kitten(name='fluffy', sound='rawr')
    a1 = Duck(name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans')

    hello = RevStr('Iqbal loves Thalia')
    print(hello)


if __name__ == '__main__': main()