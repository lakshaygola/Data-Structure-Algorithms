"""Problem statement: - we have sequence of words as a string. First word is all in smaller cases then starting letter
            of each word in Capital letter. We have to calculate the total words present in the string.
            """
import re
# Function to solve the problem
def camelcase(s):
    if len(s) > 0:
        count = 1
    else:
        return 0
    for i in range(len(s)):
        if not s[i].islower():
            count = count + 1
    return count

# Test cases 1
#string1 = 'saveChangesInTheEditor'
#print(camelcase(string1))


"""Problem statement:- So we have a string which reperesnt the password of the user we have to make the password strong.
                Password will only be strong when
                1. The lenght of the string is 6 or more than that
                2. Have at least one lower case character
                3. Have at least one upper case character
                4. Have at least one number in it 
                5. And should have one or more special charater
                we have to find that how many minimum charater is required to make user password strong."""


# Function to solve the above problem
def minimumNumber(n , password):              # n- lenght of string, s- string
    count, i = 0, 0
    numDone, specialDone, upperDone, lowerDone = False, False, False, False
    while i < n:
        if not numDone:
            if password[i].isdigit():
                numDone = True
                count = count + 1
                i = i + 1
        #print('number: ', count)
        if not specialDone:
            regspecial= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not (regspecial.search(password) == None):
                specialDone = True
                count = count + 1
                i = i + 1
        #print('special: ', count)
        if not upperDone:
            if password[i].isupper():
                upperDone = True
                count = count + 1
                i = i+1
        #print('upper: ', count)
        if not lowerDone:
            if password[i].islower():
                lowerDone = True
                count = count + 1
                i = i + 1
        #print('lower: ', count)
    if n < 6:
        n = n + count
        rem = 6 - n
        #print('remaining: ',rem)
        count = count +rem

    return count

num = '1234567890'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
special = '@_!#$%^&*()<>\?/|}{~:'
# Optimial solution of the problem
def minimumNumber1(n, password):
    count = 0
    if all(n not in password for n in num):
        count= count + 1
    if all(l not in password for l in lower):
        count= count + 1
    if all(u not in password for u in upper):
        count = count + 1
    if all(s not in password for s in special):
        count = count + 1
    count = count + max(0, 6-n)

    return count

# Test case 1
string1 = 'Ab1'
n1= len(string1)
#print(minimumNumber1(n1 , string1))


# Test Case 2
string2 = '#HackerRank'
n2 = len(string2)
print(minimumNumber1(n2, string2))