'''
Dictionaries are collections holding key-value pairs
Like Java's hashmap, for example.

https://www.geeksforgeeks.org/python-add-new-keys-to-a-dictionary/
- Look at the section for using the * method
    - It'll make a new dict, taking all values from previous dict
'''

def main():
    # animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'rawr',
    # 'giraffe': '...', 'dragon': 'screech'}

    # same results can be found by doing:
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'rawr',
        giraffe = '...', dragon = 'screech')

    # for k in animals.keys(): print(k)     <-- just for keys
    # for v in animals.values(): print(v)   <-- just for values
    # print(animals.get('godzilla'))        <-- will give 'None' instead of error
    
    animals['monkey'] = 'haha' # inserts to a dictionary
    # print(animals['monkey'])
    # print('found!' if 'godzilla' in animals else 'nope!')

    print_dict(animals)

def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')

if __name__=='__main__': main()
