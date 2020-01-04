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