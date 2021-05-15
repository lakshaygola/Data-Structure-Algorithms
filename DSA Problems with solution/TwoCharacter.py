"""Problem statement:- We have a string and we can remove as many character as we want to achieve max length of the
            string such that string contain only two consecutive element. And the we have to remove all the instance of
            choose character from the string."""

import collections

# Function to solve the above problem
def alternative(s):
    valid_string = collections.Counter(s)
    keys= []
    maxLength = 0
    while not len(collections.Counter(valid_string)) == 2:
        for key in valid_string:
            keys.append(key)
        for char in range(len(keys)-1):
            for char_ in range(char+1, len(keys)):
                string = s
                string = string.replace(keys[char], '')
                string = string.replace(keys[char_], '')
                result= isvalid(string)
                if result:
                    if len(string) > maxLength:
                        maxLength = len(string)
                        valid_string = string
    return maxLength


# Function to check the string created after removal of the character is valid or not
def isvalid(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


# May be optimize solution of the problem
def alternate(s):
    if len(s) ==2:
        if isvalid(s):
            return 2
    maxLength = 0
    character = list(set(s))
    for char in range(len(character)-1):
        for char_ in range(char+1, len(character)-1):
            string = [ch for ch in s if ch == character[char] or ch == character[char_]]
            if isvalid(string):
                maxLength = max(maxLength, len(string))
    character.clear()
    return maxLength



# Test case 1
string1 = 'abaacdabd'
print('abaacdabd: ', alternate(string1))

# Test Case 2
string2 = 'beabeefeab'
print('beabeefeab: ',alternate(string2))

# Test case 3
string3 = 'asdcbsdcagfsdbgdfanfghbsfdab'
print('asdcbsdcagfsdbgdfanfghbsfdab: ', alternate(string3))

# Test Case 4
string4 = 'ab'
print('ab', alternate(string4))