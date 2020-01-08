'''
Dictionaries are collections holding key-value pairs
Like Java's hashmap, for example.
Dictionaries are 
'''

def main():
    animals = {'kitten': 'meow', ' puppy': 'ruff!', 'lion': 'rawr',
    'giraffe': '...', 'dragon': 'screech'}
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')