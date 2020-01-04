''' 
The different data types in python
python uses 'ducktyping', "if it walks like a duck it's that"
Look at the type of the following: 
'''

from decimal import *

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