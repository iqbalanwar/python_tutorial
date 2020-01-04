
def main():
    x = ('meow', 'grrr', 'purr')
    kitten(*x) # this is a pass by reference to x

def kitten(*args): # variable length argument list
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__=='__main__': main()
