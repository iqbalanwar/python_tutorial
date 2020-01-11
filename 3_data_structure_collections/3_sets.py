'''
A set is like a list that doesn't allow duplicate elements.
'''

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

# just write __main for this block in VSCode:
if __name__ == "__main__": main()