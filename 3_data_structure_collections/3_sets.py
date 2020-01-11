'''
A set is like a list that doesn't allow duplicate elements.
If you print a string set, you'll get an unordered list of the
unique characters in that string.

You can sort those characters by writing sorted(paramName)

print_set(a - b) will give the members in set a that aren't in b
print_set(a | b) will give members that are in one or both sets
print_set(a ^ b) will give members that are in a or b, but not both
print_set(a & b) will give members that are in both sets
'''

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(sorted(a))
    print_set(b)

    print_set(a - b)
    print_set(a | b)
    print_set(a ^ b)
    print_set(a & b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

# just write __main for this block in VSCode:
if __name__ == "__main__": main()
