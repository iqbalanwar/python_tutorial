'''
Keyword arguments are basically dictionaries
'''

def main():
    x = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    kitten(**x) # a reference to keyword arguments the dictionary

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__=='__main__': main()
