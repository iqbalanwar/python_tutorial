# this is a hackerrank problem I'm doing on my own

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c)-1:
        # if 2 cloud jumps
        if i+2 < len(c) and c[i+2] == 0:
            i += 1
        jumps += 1
        i += 1
    return jumps


def main():
    result = jumpingOnClouds((0, 0, 1, 0, 0, 1, 0))
    print(f'The total jumps is {result}')

    # presidents = ["Washington", "Adams", "Jefferson",
    #               "Madison", "Monroe", "Adams", "Jackson"]
    # for num, name in enumerate(presidents, start=1):
    #     print("President {}: {}".format(num, name))

if __name__ == '__main__': main()
