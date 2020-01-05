# This program is a tutorial of python 3
# This follows the VSCode Python tutorial 

# In python, everything is an object, including strings

msg = "hello world"
msg.capitalize()
msg.split()
print(msg.capitalize())

val = 69
print("420 blaze, {}".format(val))

# name = 'World'  # string interpolation can also be written as:
# program = 'Python'
# print(f'Hello {name}! This is {program}')

# How blocks work:
# Note: Scope is not defined in blocks.
# Scope is defined in functions, objects, and modules
x = 1
y = 2
if x < y:
    z = 3
    print("I've printed out {}".format(z))
print(z)

# while loop:
def fizzbuzz(value):
    i = 1
    while i <= value:
        if (i % 15) == 0:
            print("fizzbuzz is on {}".format(i))
        elif (i % 3) == 0:
            print("fizz is on {}".format(i))
        elif (i % 5) == 0:
            print("buzz is on {}".format(i))
        i += 1

fizzbuzz(100)

# for loop:
words = ['one','two','three','four','five']

for i in words:
    print(i)

# ============================================ functions: ============================================
def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range(100):
        if isPrime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()

n = 13
if isPrime(n):
    print('{} is prime'.format(n))
else:
    print('{} not prime'.format(n))
