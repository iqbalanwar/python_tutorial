'''
A decorator is a special type of function that returns a wrapper
function. Remember, in python, everything is an object (this 
includes functions).
'''

import time

# THIS IS AN EXAMPLE OF SCOPE:
def f1():
    print('This is f1')

def wrapperFunc():
    def innerFunc():
        '''
        The function innerFunc only exists within the scope of 
        wrapperFunc. This is an object, created within wrapperFunc,
        so it cannot be called outside this function
        '''
        print('This is innerFunc')
    return innerFunc

x = f1 # So x is taking the f1 object (which is a function)
x()
y = wrapperFunc()
y()
# innerFunc() <-- throws a name error, because it's not initialized

print('==================================')
# ================= DECORATOR FUNCTIONS: =================

# THE FOLLOWING IS AN EXAMPLE OF DECORATOR FUNCTIONS:
def d1(d):
    def d2():
        print('This is before the function call')
        d()
        print('This is after the function call')
    return d2

@d1
def decorator():
    print('This is the decorator function')

decorator()

'''
So what does @d1 do? It takes the function called after it is used,
and passes it as a parameter to it. By doing this, it assigns (and 
returns) that function (in this case called decorator) to the wrapper
itself (d1).
So it's essentially doing this:

x = d1(decorator)
x()

How is this useful? The following uses the 'import time' given above.
Look at the following:
'''

print('==================================')


def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper

@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum() # Does the same thing as:
    # elapsed_time(big_sum())

if __name__ == '__main__': main()
