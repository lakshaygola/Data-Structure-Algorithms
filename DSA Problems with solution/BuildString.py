"""Problem statement :- We have a string which is initially emtpy we can perform following operation in order to make a
                string
                1. We can add the element at the end of the string which cost A dollars
                2. We can copy and append substring at the end of the string which cost B dollars
                We have to find the minimum cost in which string can be build."""

# Helper function
def findSubstring(s1, s2):
    sub1, sub2 = [], []
    i = 0
    # For 2nd string
    for j in range(i+1, len(s2)+1):
        sub2.append(s2[i:j])

    # For 1 String
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+1):
            sub1.append(s1[i:j])

    for string in sub2:
        if string in sub1:
            return string
    return s2[0]

# Function to solve the problem
def buildString(s, size, A, B):
    i, j = 0, size-1
    cost = A
    if size == 0:
        return 0
    while i < size:
        while i < j:
            substring = findSubstring(s[:i], s[i:j+1])
            if len(substring) > 1:
                cost += B
                i += j
            elif len(substring) == 1:
                cost += min(A, B)
                i += 1
    return cost


# Test case 1
string1= 'aabaacaba'
size1= len(string1)
A, B = 4, 5
print(buildString(string1, size1, A, B))

