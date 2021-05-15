"""Problem statement: - We have to find out the given string is valid or not. The given string is valid only if one of
            these cases is true
            1. All the character appears the same number of times
            2. String will also valid if we remove only one element and the remaining character will occur same number
            of time."""

import collections

# Function to remove the element from the list
def RemoveOne(string, char):
    for pos in range(len(string)):
        if string[pos] == char:
            string = string.replace(char , '' , 1)
            break
    return string


# Function to check weather string is valid or not
def isValid(s):
    sCopy = s
    characters = list(set(s))
    for char in range(len(characters)):
        countChar = collections.Counter(sCopy)
        if len(list(set(countChar.values()))) == 1:
            return "Yes"
        sCopy = RemoveOne(s , characters[char])
    return 'No'


# Test case 1
string1= 'aabbcd'
print(isValid(string1))

# Test Case 2
string2= 'aabbccddeefghi'
print(isValid(string2))

# Test case 3
string3 = 'abcdefghhgfedecba'
print(isValid(string3))

# Test case 4
string4 = 'ab'
print(isValid(string4))

# Test case 5
string5 = 'abbac'
print(isValid(string5))
