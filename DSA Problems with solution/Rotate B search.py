# Function to count number of rotation in the list
def binarysearch(nums, target):
    lo, hi= 0, len(nums)-1
    while(lo<=hi):

        mid= (lo+hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo= mid+1
        else:
            hi= mid-1
    return -1

def count_rotation(nums):
    lo, hi= 0, len(nums)-1

    while lo <= hi:
        mid= (lo+hi) // 2
        if mid > 0 and nums[mid] < nums[mid-1]:
            return mid
        elif nums[mid] < nums[len(nums)-1]:
            hi= mid-1
        else:
            lo= mid+1

    return mid

def rotate_ls(nums, target, rotate):
    left= nums[:rotate]
    right= nums[rotate:]
    result1= int(binarysearch(left, target))
    result2 = int(binarysearch(right, target))
    if result1 == -1:
        result1= len(left)-1
    else:
        if result2 == -1:
            result2= 0
        else:
            result2= result2 + 1
    print(result1, result2)
    result= result1 + result2
    if result == -1:
        print('Element for which you are searching for is NOT FOUND in the list')
    else:
        print('Element for which you are searching for in FOUND at index: ', result)


nums= [4,5,6,7,0,1,2]
target= int(input('Enter the Number you want to serach: '))
rotate= count_rotation(nums)
rotate_ls(nums, target, rotate)