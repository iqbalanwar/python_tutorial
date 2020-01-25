import math


def binarySearch(numList, left, right, x):

  # Checks if the size of the list is greater than or equal to 1
  # Because if it isn't, x isn't in the list
  if right >= left:

    # This keeps of the index from the original numList
    anchor = left + math.floor((right - left)/2)

    if x == numList[anchor]:
      print(anchor)

    elif x > numList[anchor]:
      return binarySearch(numList, anchor+1, right, x)

    elif x < numList[anchor]:
      return binarySearch(numList, left, anchor-1, x)

  else:
    print("Element is not in list")


def main():
  numList = [1, 3, 4, 6, 8, 9, 12, 21, 34, 37, 45, 102, 256]
  listLen = len(numList)-1

  print("The index location of 4 in numList is ", end="")
  binarySearch(numList, 0, listLen, 4)
  
  print("The index location of 102 in numList is ", end="")
  binarySearch(numList, 0, listLen, 102)


if __name__ == '__main__': main()