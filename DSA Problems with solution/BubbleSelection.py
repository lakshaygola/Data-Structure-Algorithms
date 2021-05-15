"""Bubble sorting and Selection sorting"""
# Selection sorting:- select the smallest number from the unsorted list and place it on first index repeat untill you
# get the sorted one

# Function perform selection sort (recursivly)
def recSelectionSorting(nums):
    if len(nums) < 1:
        return nums
    minNumber = min(nums)
    minNumber_idx = nums.index(minNumber)
    nums[minNumber_idx], nums[0] = nums[0], nums[minNumber_idx]
    nums += recSelectionSorting(nums[1:])
    return nums

# Iteration method
def selectionSorting(nums):
    if len(nums) < 2:
        return nums
    for i in range(len(nums1)):
        j = nums.index(min(nums[i:]))
        nums[j], nums[i] = nums[i], nums[j]
    return nums


# Function to perform the bubble sort
def bubbleSorting(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Test case 1
nums1 = [64, 25, 12, 22, 11]
print(bubbleSorting(nums1))

# Test Case 2
nums2= [78,1,235,568,12,0,78,3,2,554]
print(bubbleSorting(nums2))

# Test case 3
nums3 = []
print(bubbleSorting(nums3))

# Test case 4
nums4 = [1]
print(bubbleSorting(nums4))

# Test Case 5
nums5 = [45, 42, 38, 31, 25, 20, 16, 12, 9, 3, 1]
print(bubbleSorting(nums5))
