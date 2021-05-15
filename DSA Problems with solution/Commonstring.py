"""Problem statement: - String can be a child of another string if it can be formed by deleting 0 or more character and
                    the letter can not be rearranged. We have to find the longest child the both string of same length
                    can be formed.(Longest common subsequence)"""

# Function to solve the Problem (recursive solution)
def recCommonChild(s1, s2, i= 0, j = 0):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + recCommonChild(s1, s2, i+1, j+1)
    else:
        return max(recCommonChild(s1, s2, i+1, j), recCommonChild(s1, s2, i, j+1))
# As recursion take to much time. So we have to this iterative solution

# Function to solve the problem (iterative method)
def commonChild(s1, s2):
    memo = {}
    def lcs(i= 0 , j= 0):
        key = (i, j)
        if key in memo:
            return memo[key]
        if i == len(s1) or j == len(s2):
            memo[key] = 0
        elif s1[i] == s2[j]:
            memo[key]= 1 + lcs(i+1, j+1)
        else:
            memo[key] = max(lcs(i+1, j), lcs(i, j+1))
        return memo[key]

    return lcs(0 ,0)

# Helper Function of the dynamic programming solution
def get_value(result, i, j):
    if i <= 0 and j <= 0:
        return 0
    else:
        return result[i][j]

# Still its a slow method
def CommonChild(s1, s2):
    result = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                result[i][j] = 1 + result[i-1][j-1]
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])
    return result[-1][-1]



# Test case 1
s1 = 'SHINCHAN'
s2 = 'NOHARAAA'
print(CommonChild(s1, s2))