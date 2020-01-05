'''
Generator functions serve as iterators; they return a stream 
of values instead of a single value. If you need a series of
values returned from a function, generators are the way to go
'''

def main():
    '''
    Problem being solved: the built-in function range(25)
    returns numbers from 0 to 24, not including 25. The 
    function created is "inclusive_range", which is like 
    range but includes up to the number provided.
    '''
    for i in inclusive_range(25):
        print(i, end = ' ') # end = ' ' keeps everything in one line
    print()


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        # yield is like return, except for generators
        # It yields a value, then the function continues
        # until it yields the next value
        yield i
        i += step


if __name__ == '__main__': main()