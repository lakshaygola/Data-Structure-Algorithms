"""Quick Sort"""

# Function which perform quick sort on the given array (inplace sorting -  no extra space created)
def quickSorting(lower, higher, nums, count = 0):
    if lower < higher:
        pivot_idx, count = partition(lower, higher, nums, count)
        quickSorting(lower, pivot_idx-1, nums, count)
        quickSorting(pivot_idx+1, higher, nums, count)
    return (nums, count)

# Partition function which help to divide the list
def partition(start, end, nums, count):
    pivot_idx = start
    pivot = nums[pivot_idx]

    while start < end:
        while start < len(nums) and nums[start] <= pivot:
            start += 1
        while nums[end] > pivot:
            end -= 1
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]
            count += 1
    nums[end], nums[pivot_idx] = nums[pivot_idx], nums[end]
    count += 1

    return (end, count)



# Test case 1
arr1 = [4, 5, 3, 7, 2]
print(quickSorting(0, len(arr1)-1, arr1))

# Test case 2
arr2 = [15, 6, 2, 3, 10, 5, 9]
print(quickSorting(0, len(arr2)-1, arr2))

# Test case 3
arr3 = []
print(quickSorting(0, len(arr3)-1, arr3))

# Test case 4
arr4 = [1]
print(quickSorting(0, len(arr4)-1, arr4))

# Test case 5
arr5 = [1, 56, 2, 3, 89, 45]
print(quickSorting(0, len(arr5)-1, arr5))
