''' 
The different data types in python
python uses 'ducktyping', "if it walks like a duck it's that"
Look at the type of the following: 
'''

from decimal import *

# ================ STRING AND NUMERICAL DATA TYPES ================

x = 7 / 3
# x = 7 // 3 <- returns a whole
# x = 7.0
# x = "seven, {}, {}".format(8, 9) # single and double quotes are the same
# a = 8
# b = 9
# x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))

# y = .1 + .1 + .1 - .3
a = Decimal('.10')
b = Decimal('.30')
y = a + a + a - b
print('y is {}'.format(y))
print(type(y))



print("================================")
# ================ BOOLEAN ================

x = 1 # x = 0 would be false
print(f'x is {x}')
print(type(x))

if x:
    print("True")
else:
    print("False")



print("================================")
# ================ SEQUENCE TYPES (List, Tuples, Dictionaries) ================

# =====> List:
# LISTS ARE MUTABLE
x = [ 1, 2, 3, 4, 5 ]
x[4] = 9001
for i in x:
    print(f'i is {i}')

print("----------")

# =====> Tuple: (NOT IMMUTABLE)
# NOTE: TUPLES ARE FAVORED OVER LISTS, BECAUSE THEY'RE NOT IMMUTABLE
y = ( 1, 2, 3, 4, 5 )
# y[4] = 9001 <-- WILL THROW AN ERROR, TUPLES ARE IMMUTABLE
for i in y:
    print(f'i is {i}')

print("----------")

# =====> Range:
# z = range(5)
z = range(5, 50, 5) # start - stop - step
# x[2] = 42 <-- WILL THROW AN ERROR, RANGE IS IMMUTABLE

# this is mutable:
# z = list(range(5))
# z[2] = 42

for i in z:
    print(f'i is {i}')

print("----------")

# =====> Dictionary
# DICTIONARIES ARE MUTABLE
q = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
# q['three'] = 21
for k, v in q.items():
    print(f'k: is {k}, v: is {v}')



print("================================")
# ================ type() and id() ================
# type gives the data type given
# id gives the id of the unique object created
# - So two variables can have the same items, but have different ids
# - ids are randomly generated, unique numbers
x = (1, 'two', 3.0 , [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print("The type of x[3] is {}".format(type(x[3])))
print("The id of x[0] is {}".format(id(x[0])))
print("The id of y[0] is {}".format(id(y[0])))
print('Note that they have the same values of id, because literals are the same')
print(f"However, the id of x is {id(x)}")
print(f"And the id of y is {id(y)}. See how they're different?")

if isinstance(x, tuple):
    print("x is a tuple")
elif isinstance(x, list):
    print("x is a list")
else:
    print("x is not a list or tuple")