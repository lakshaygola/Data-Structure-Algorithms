"""Problem statement- we have a string and we have to reduce it by performing certain operation if adjacent character is
                    same delete them if all the character get delete return Empty String"""

# Function to perform the above define solution
def superReduceString(s, i= 1):
    if len(s) == 0:
        return 'Empty String'
    if (i < len(s)):
        if s[i-1] == s[i]:
            s = s[:i-1] + s[i+1:]
            return superReduceString(s , 1)
        return superReduceString(s, i+1)
    return s

# Alternative function
def superReducedString(s):
    char = list(s)
    i = 0
    while i < len(char)-1:
        if char[i+1] == char[i]:
            del char[i]
            del char[i]
            i = 0
            if len(char) == 0:
                return 'Empty String'
        else:
            i = i+1
    return ''.join(char)


# Test case 1
string1 = 'aab'
print(superReduceString(string1))

# Test Case 2
string2 = 'aaabccddd'
print(superReduceString(string2))

# Test Case 3
string2 = 'aa'
print(superReduceString(string2))

# Test Case 4
string4= 'baab'
print(superReduceString(string4))

