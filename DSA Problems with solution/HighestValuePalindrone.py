"""Problem statement: - We will have a string represented in numbers and the maximum number of changes you can make in
            the string. We can alter the string to make it palindrone which have largest possible value and we can not
            alter the length of the string. And if its not possible return -1.
            example: - '1231', k = 3  -> '9339' this string have largest value and it also palindrone"""

# Using recursion for making the palindrome
def recPalindrome(nums, k, j= -1, i= 0):
    if i < j:
        if nums[i] == nums[j]:
            return recPalindrome(nums, k, j-1, i+1)
        if k > 0:
            if nums[i] > nums[j]:
                nums[j] = nums[i]
            else:
                nums[i] = nums[j]
        return recPalindrome(nums, k-1, j-1, i+1)
    return (nums, k)
# Recursion can be to memory consuming.


# Effective solution of palindrome
def makePalindrome(s, k):
    nums = list(s)
    i, j = 0, len(nums)-1
    mark = [0] * len(nums)
    while i < j:
        if nums[i] != nums[j]:
            if nums[i] > nums[j]:
                nums[j] = nums[i]
                mark[j] = 1
            else:
                nums[i] = nums[j]
                mark[i] = 1
            k -= 1
        i += 1
        j -= 1

    if k < 0 :
        return '-1'
    result = highestvalue(nums, k, mark)
    return result




# Function to find the highest value for the palindrome
def highestvalue(nums, k, mark):
    l, h = 0, len(nums)-1
    while l <= h:
        if l == h and k >= 1:
            nums[l] = '9'
            break
        if nums[l] < '9':
            # If values are not changed intially
            if mark[l] == 0 and mark[h] == 0 and k >= 2:
                nums[l] = nums[h] = '9'
                k -= 2
            # If values are already change perviously
            if (mark[l] == 1 or mark[h] == 1) and k >= 1:
                nums[l] = nums[h] = '9'
                k -= 1
        l += 1
        h -= 1
    return ''.join(nums)



# Test case 1
string1 = '1231'
k1 = 3
result1 = makePalindrome(string1, k1)
print(result1)



# Test case 2
string2 = '092282'
k2 = 3
result2 = makePalindrome(string2, k2)
print(result2)
