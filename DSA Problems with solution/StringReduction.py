"""Problem statement: - We have a string consist a,b and c letters. We can perform the following operation on it
                Two adjacent letter can be replace by thrid letter and we have to find the shortest string which can be
                formed by performing the operation"""

import collections

# Helper function to find the character to replace the string
def findChar(ch1, ch2):
    character = ['a', 'b', 'c']
    for i in range(len(character)):
        if character[i] == ch1 or character[i] == ch2:
            pass
        else:
            return character[i]


# Function to perform the problem
def stringReduction(s):
    character = dict(collections.Counter(s))
    i= 0
    while len(character) != 1:
        if s[i] != s[i+1]:
            char = findChar(s[i], s[i+1])
            print('Character: ', char)
            s = s[:i] + char + s[i+2:]
            print('String After Replacement: ', s)

    return len(s)


# Optimal solution
def StringReduction(s):
    character = dict(collections.Counter(s))
    print(character)
    even = odd = other = 0
    if len(character) == 1:
        return len(s)
    # Checking that all values are even
    for value in character.values():
        if value % 2 == 0:
            even += 1
        elif value % 2 != 0 or value == 1:
            odd += 1
        else:
            other += 1
    if even == 3 or odd == 3:
        return 2
    else:
        return 1


# Test Case 1
string1 = 'aba'
#print(StringReduction(string1))

# Test Case 2
string2 = 'abababaccc'
print(stringReduction(string2))

# Test Case
string3 = 'ccccc'
#print(StringReduction(string3))