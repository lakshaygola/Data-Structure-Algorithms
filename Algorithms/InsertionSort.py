"""Insertion Sort"""

def insertionSorting(nums):
    count = 0
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j+1], nums[j] = nums[j], key
            j -= 1
            count += 1
        nums[j+1] = key
    return (nums, count)




# Test Case 1
num1 = [1,2,3,4,5,6]
result1 = insertionSorting(num1)
print('Sorted : ', result1[0], 'No of swaping: ' , result1[1])

# Test case 2
num2= [10,9,8,7,6,5,4,3,2,1]
result2 = insertionSorting(num2)

# Test case 3
num3= []
print(insertionSorting(num3))

# Test Case 4
num4= [88,25,3,1,56,87,32,9,41]
print(insertionSorting(num4))