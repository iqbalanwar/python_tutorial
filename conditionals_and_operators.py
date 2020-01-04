''' 
The following explores conditional statements and operators.
The types of operators are comparison, logical, identity, and membership:

comparison:
==, != , <= , >= , < , >

logical:
and, or, not

identity: (checks if two objects are the same or not)
x is y     <-- true if the same object
x is not y <-- true if not the same object

membership: (true if a variable is a member of a collection)
x in y     <-- true if x is a member of collection y
x not in y <-- true if x is not a member of collection y
'''

hungry = True
# Ternary operator:
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)


# ======================== Arithmetic Operators ========================
x = 5
y = 3
z = x / y
# z = x // y
# z = x % y
pos_z = -z
neg_z = +z
print(f'result is {z}')
print(f'positive z result is {pos_z}')
print(f'negative z result is {neg_z}')


print("========================")
# ======================== Bitwise Operators ========================
'''
& represents And, | represents Or, ^ represents Xor
<< represents shift left, >> represents shift right

For &, the bits must be the same to be 1, otherwise 0
For |, the bits need at least one to be 1, otherwise 0
For ^, the result will have a bit set if one or the other,
    not both, have the bit set
For << and >>, the bits get shifted by the amount given
'''
x = 0x0a
y = 0x02
z = x & y 
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
# for &, the bits must be the same to be 1, otherwise 0


print("========================")
# ======================== Boolean Operators ========================
'''
'and' represents And, 'or' represents Or, 'not' represents Not, 
'in' represents Value in set, 
'not' in represents Value not in set,
'is' represents the Same object identity, 
'is not' represents Not same object identity
'''
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'
if y in x:
    print("Expression is true")
else:
    print("Expression is false")

if y is x[1]:
    print("Expression is true")
else:
    print("Expression is false")