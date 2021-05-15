"""Problem statement: - In the we have two different sequence from which we have to find out the longest common subsequ-
                        ence from both the sequence. And we have to write the effective code for the problem."""


# Basic function to find the LCS for the sequence (using recursive method)
def lcs_basic(seq1, seq2, i=0, j=0):
    if i == len(seq1) or j == len(seq2):
        return 0
    else:
        if seq1[i] == seq2[j]:
            return 1 + lcs_basic(seq1, seq2, i+1, j+1)
        else:
            return max(lcs_basic(seq1, seq2, i+1, j), lcs_basic(seq1, seq2, i, j+1))
# Time complexity of the basic lcs function is O(2^(m+n)) where m and n is the length of the sequences we have
# This time complexity of the function is to big


# Function which effectively perform the lcs function using memoization technique
def eff_lcs(seq1, seq2):
    memo= {}                       # As this is dynamic approach to the problem so we will store the intermediate result

    def lcs(i, j):
        key= (i, j)
        if key in memo:
            return memo[key]
        if i == len(seq1) or j == len(seq2):
            memo[key]= 0
        elif seq1[i] == seq2[j]:
            memo[key]= 1+ lcs(i+1, j+1)
        else:
            memo[key]=  max(lcs(i+1, j), lcs(i, j+1))

        return memo[key]
    return lcs(0, 0)
#Time complexity of the approach is O(m*n) which is must lesser than recursive approach (m and n are the size of strings)


# Helper function for the dynamic solution
#This function return 0 if index in the matrix is less than 0 otherwise it return the values which is store at that index
def get_value(matrix, i, j):
    if i <= 0 and j <= 0:
        return 0
    else:
        return matrix[i][j]


# Function which apply the dynamic solution to the problem
def dynamic_lcs(seq1, seq2):
    size1= len(seq1)
    size2= len(seq2)
    result= [[0 for _ in range(size1)] for _ in range(size2)]
    if size1 == 0 or size2 == 0:
        return 0
    for i in range(size2):
        for j in range(size1):
            if seq1[i-1] == seq2[j-1]:
                result[i][j]= 1 + get_value(result, i-1, j-1)
            else:
                result[i][j]= max(get_value(result, i-1, j), get_value(result, i, j-1))
    return result[-1][-1]

seq1= 'serendipitous'
seq2= 'precipitation'
print('Sequence 1: ', seq1)
print('Sequence 2: ', seq2)
print('Longest Common Subsequence: ', dynamic_lcs(seq1, seq2))


s1= 'SHINCHAN'
s2= 'NOHARAAA'
print('Sequence 1: ', s1)
print('Sequence 2: ', s2)
print('Longest Common Subsequence: ', dynamic_lcs(s1, s2))