"""Problem statement: - we have a list of number which is we have to find the pair of the numbers so that difference
                    between the number is smallest."""

# Function to calculate the minimum possible difference b/w elements (Helper Function)
def minDifference(numbers):
    diff = float('inf')
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) < diff:
            diff = abs(numbers[i] - numbers[i+1])
    return diff



# Function to  solve the above problem
def closetNumber(nums):
    nums.sort()
    minDiff= minDifference(nums)
    numberList = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if abs(nums[i] - nums[j]) == minDiff:
                numberList.append(nums[i])
                numberList.append(nums[j])
    return numberList



# Test Case 1
arr1 = [1, 2, 3, 4, 5]
print(closetNumber(arr1))

# Test Case 2
arr2 = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
print(closetNumber(arr2))

# Test Case 3
arr3 = [5, 4, 3, 2]
print(closetNumber(arr3))



