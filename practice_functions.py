# THE FOLLOWING IS MY PRACTICE WITH SOME FUNCTIONS USING PYTHON

def main():
    
    bigOrSmallString("hi lol")
    oddOrEvenString("hi lol")

    listy = [1, 3, 6, 2, 5, 8, 4, 9]
    medianOfArray(listy)
    sumList(listy)

    vowelCount("onomatopoeia")
    initials("Thalia Elizabeth Santamaria Parrales")

    # Bonuses:
    # dayOfTheWeek()
    # trainLines()
    countXPairs("xHellox")

'''
PART 1: Big or Small String?
You may have to dig into some documentation for some of these!
Write a function called bigOrSmallString that accepts one argument, 
a string, and returns "This word is loooooong!" if the string's 
length is greater than 10, and "This word is short" otherwise.
'''
def bigOrSmallString(str):
    print(f"'{str}' is a loooooong string!\n") if len(str) > 10 else print(f"'{str}' is a short string.\n")

'''
PART 2: Odd or Even String Length?
Write a function called oddOrEvenString that accepts one argument, 
a string, and returns "This string's length is odd.." if the length 
is an odd number, and "This string length is TOTALLY even!" if the 
string length is even.
'''
def oddOrEvenString(str):
    print(f"'{str}' is an odd numbered string...\n") if (len(str) % 2) != 0 else print(f"'{str}' is a TOTALLY even numbered string!\n")

'''
PART 3: Median
Write a function called medianOfArray that takes a list (array) as an argument.
The function should return the median number in an array. Hmmmm, haven't
you found a median of the array before? Maybe not..

Hint: Use some kind of sorting method to put the values in order first, 
then somehow access the median element, somehow using the length of the 
array....maybe? We're going to go over arrays in depth on Monday but see 
if you can find some Array methods that can accomplish what you need.
'''
def medianOfArray(someList):
    listy = sorted(someList) # sorts in place, mutates the list

    i = int(len(listy)/2) # for some reason, len(listy) / 2 is a float, not int
    # type casting to an int rounds down
    
    median = 0
    if len(listy) == 1:
        median = listy[0]
    elif (len(listy) % 2) != 0:
        median = listy[i]
    else:
        median = (listy[i - 1] + listy[i]) / 2
    print(f'The median of the passed, sorted list is {median}\n')


'''
PART 4: Sum List
Create a function called sumList that takes an list listy as an argument
and returns the sum of all the numbers in the list. If the list is empty 
then return 0.
'''
def sumList(listy):
    sum = 0
    for i in listy:
        sum += i
    print(f'The sum of the given list is {sum}\n')

'''
PART 5: Vowel Count
Create a function called vowelCount that accepts a str as an argument and
returns the number of vowels in that string.
'''
def vowelCount(str):
    strLowercase = str.lower()
    numVowels = 0

    for i in strLowercase:
        if ( (i == 'a') | (i == 'e') | (i == 'i') | (i == 'o') | (i == 'u') ):
            numVowels += 1
    print(f'There are {numVowels} vowels in {str}\n')


'''
PART 6: Initials
Write a function called initials that accepts one argument (person's name) and
returns their initials.

It should work both with and without middle name being provided.
Hint! Remember, string methods? Use them!

initials('Neil Patrick Harris');
// N.P.H.
'''
def initials(fullName):
    splitName = fullName.split(' ')
    nameInitials = ''
    for i in splitName:
        nameInitials += i[0] + '.'
    print(f'The name {fullName} has the initials {nameInitials}\n')


# BONUSES!!
'''
Days of the week
Write a function that prompts the user to specify what day is today.

If it's Monday alert "Energize!"
If it's Tuesday alert "Just getting started!"
If it's Wednesday alert "Hump Day!"
If it's Thursday alert "Almost there!"
If it's Friday, Saturday or Sunday alert "Weeeeeee!"
If it's not anything above alert "Huh, sorry didn't get that?"
'''
def dayOfTheWeek():
    dayOfWeek = input("Which day of the week is today? Please enter the full day! ")
    day = dayOfWeek.lower()

    if day == 'monday':
        print("Energize!\n")
    elif day == 'tuesday':
        print("Just getting started\n")
    elif day == 'wednesday':
        print("Hump Day!\n")
    elif day == 'thursday':
        print("Almost there!!\n")
    elif (day == 'friday') | (day == 'saturday') | (day == 'sunday'):
        print("Weeeeeee!!!\n")
    else:
        print("Please input a day of the week only...")
        dayOfTheWeek()

'''
Let's take the Subway
Write out a function that would do the following

When the script is run, a menu should be prompted displaying:

A list of three trains - The (L) Train, The (N) Train, The (S) Train
And asking the user to make their selection!
THEN:

If the user enters: L

A message should output a message containing the user's selection labeled 
as L train and display the following stops:
8th Ave
6th Ave
Union Square
3rd Ave
1st Ave
Bedford Ave
If the user enters: N
A message should output a message containing the user's selection labeled 
as N train and display the following stops:
Times Square
Herald Square
28th St
23rd St - DAPS Nexus
Union Square
8th St
If the user enters S
A message should output a message containing the user's selection labeled 
as S train and display the following stops:
Grand Central 42nd st
Times Square 42nd St
Finally, a Thank You message should alert.

The program then exits.
'''
def trainLines():
    userLine = input("Which train line are you taking (Please input L, N, or S)? ")
    train = userLine.lower()

    l_train = ("8th Ave", "6th Ave", "Union Square", "3rd Ave", "1st Ave", "Bedford Ave")
    n_train = ("Times Square", "Herald Square", "28th St", "23rd St - DAPS Nexus", "Union Square", "8th St")
    s_train = ("Times Square 42nd St", "Grand Central 42nd St")
    
    print(f"The {userLine.upper()} train goes to the following stops:")
    if train == 'l':
        for i in l_train:
            print(f"    {i}")
    elif train == 'n':
        for i in n_train:
            print(f"    {i}")
    elif train == 's':
        for i in s_train:
            print(f"    {i}")

    print("Thank you!\n")

'''
Double X Counter
Write a function called countXx. Count the number of "xx" in the given string. We'll say that overlapping is allowed, so "xxx" contains 2 "xx".

  countXx('abcxx')
  // 1
  countXx('xxx')
  // 2
  countXx('xxxx')
  // 3
'''
def countXPairs(str):
    pairs = 0
    
    if len(str) < 2:
        print("This string isn't long enough!")
    elif len(str) == 2:
        if (str[0] == 'x') & (str[1] == 'x'):
            pairs += 1
    else:
        for i in range(1, len(str)):
            # if str[i-1] == str[i]: <--- THIS IS FOR ALL PAIRS
            if (str[i-1] == 'x') & (str[i] == 'x'):
                pairs += 1

    print(f"There are {pairs} pairs of xx in the string {str}")


if __name__ == "__main__": main()