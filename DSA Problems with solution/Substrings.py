"""Problem Statement :- We have a string and we have to find out all the possible substrings we can get from that string
                        substring should be in continuous order in the main string"""

# Function to print all possible substrings recursively
def recsubstrings(string, n, idx = 0, i = 1):
    if idx <= n:
        sub = string[idx : i]
        if len(sub) >0:
            print(sub)
        recsubstrings(string, n, idx, i+1) if i< n else recsubstrings(string, n, idx+1, i = 1)


# Function to apply substrings using iteration
def itersubstring(string, n):

    substrings = [string[idx : i] for idx in range(n) for i in range(idx+1, n+1)]

    return substrings
# Time complexity of the this function is O(n^2)

# Search for the optimal solution


# s1 - main string for which we have to find the substrings (example 1)
s1 = 'abcac'
size1 = len(s1)
i, j = 0, 0
recsubstrings(s1, size1, i, j)

# Example 2
s2 = 'geeks'
size2= len(s2)
result = itersubstring(s2, size2)
print(result)




