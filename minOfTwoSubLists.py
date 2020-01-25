'''
I worked on this problem:
https: // www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
'''

def diffOfSums(numList, i, sumCalc, sumTotal):
    # This function will recurse through numList

    # if the element at this index is the last element
    if i == 0:
        # sum of the first sublist is sumCalc
        sumOne = sumCalc
        # sum of the second sublist is sumTotal - sumCalc
        sumTwo = sumTotal - sumCalc
        # The difference of the two sums would then be the absolute value,
        # between sumOne - sumTwo. Absolute value is used so the difference is
        # the same, whether sumOne or sumTwo is bigger
        return abs(sumOne - sumTwo)

    # For each element in numList, we have the choice
    # include it in the first list, or not include it
    # Whatever the case, I want the minimum result
    # from those two choices
    return min(diffOfSums(numList, i-1, sumCalc + numList[i-1], sumTotal), diffOfSums(numList, i-1, sumCalc, sumTotal))

def totalSumOfList(numList):
    sumTotal = 0
    for i in numList:
        sumTotal = sumTotal + i

    listLen = len(numList)
    return diffOfSums(numList, listLen, 0, sumTotal)


def main():
    numList = [2, 7, 12, 11, 9]
    print("The minimum difference between two lists is ", end="")
    print(totalSumOfList(numList))


if __name__ == '__main__': main()
