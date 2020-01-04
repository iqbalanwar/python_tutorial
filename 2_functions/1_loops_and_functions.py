'''
while loops, for loops,
continue, break,
functions
'''
# ======================= LOOPS =======================

secret = 'downbad'
pw = ''
# auth = False
# count = 0
# max_attempt = 5
# while pw != secret:
#     count += 1
#     if count > max_attempt: break
#     if count == 3: continue # continue skips the step
#     pw = input(f"{count}: What's the secret word? ")
# else: # loop exits normally, so the break didn't happen
#     auth = True
# print("Authorized" if auth else "You've used 5 attempts! You're locked.")


animals = ('bear','bunny','dog','cat','velociraptor')
# for pet in animals:
#     if pet == 'dog': continue
#     if pet == 'cat': break
#     print(pet)
# else: # loop exits normally, so the break didn't happen
#     print('that is all the animals')


# ======================= FUNCTIONS =======================

def main():
    x = [5]
    kitten(x)
    print(f'in main: x is {x}')
    # x = kitten()
    # print(x) # if kitten doesn't return anything, this would return None
    mutable()

def mutable():
    '''
    In the following, when assigning a mutable object to a variable
    you're actually setting a reference to the mutable object. As shown
    here, even though x isn't being directly modified, y[0] is, since x
    has been assigned to y, and x is a list (which is mutable), x also 
    changes. You can see their ids are the same, so the objects are also
    the same. Which means that the object of x and y are now the same,
    since x is a (mutable) list. This is named "call by reference".
    NOTE: Integers are not mutable.
    NOTE: Functions work exactly the same way. Look at how main calls
    kitten(). x in main is defined as the list [5], but kitten modifies the
    value of x to be [3]. Therefore, x in main is also changed to [3]
    '''
    print("===THE FOLLOWING IS FROM mutable()===")
    x = [5]
    y = x
    y[0] = 9
    print(id(x))
    print(id(y))
    print(x)
    print(y)

def kitten(a):
    a[0] = 3
    print('Meow')
    print(a)

# If this file was called as an import elsewhere,
# main in this file would be treated as a module:
if __name__=='__main__': main()