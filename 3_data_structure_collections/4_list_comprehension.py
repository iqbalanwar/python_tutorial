'''
List comprehension is a list based on another list or iterator.
- This is a common technique in python
'''

def main():
    seq = range(11) # print 0 to 10

    from math import pi
    # test these out:
    # seq2 = [x * 2 for x in seq]
    # seq2 = [x for x in seq if x % 3 != 0]
    # seq2 = [(x, x**2) for x in seq]
    # seq2 = [round(pi, i) for i in seq] <-- pi rounded by i number of decimal places
    # seq2 = { x: x**2 for x in seq } <-- cant use print_list for this
    seq2 = { x for x in 'superduper' if x not in 'pd' }
    
    # print(seq2) <-- you can only use this for the dictionary

    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == "__main__": main()
