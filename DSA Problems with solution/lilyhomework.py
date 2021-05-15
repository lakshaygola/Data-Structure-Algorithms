"""Problem statement: - We have to make the array beautiful. Array is beautiful if sum of adjacent element is minimum.
                We have to find the minimal swaps that make the array beautiful."""

# Helper function
def swaping(sortArr, arr):
    dictArr = {}
    result = 0
    for i in range(len(arr)):
        dictArr[arr[i]] = i
    #print('Inital dictonry :', dictArr)

    for i in range(len(arr)):
        #print('unsorted : ', arr, 'sorted: ', sortArr)
        if arr[i] != sortArr[i]:
            result += 1
            #print('result: ', result)
            key1, key2 = dictArr[arr[i]], dictArr[sortArr[i]]
            #print('keys: ',key1, key2)
            dictArr[arr[i]], dictArr[sortArr[i]] = key2, key1
            arr[key1], arr[key2] = arr[key2], arr[key1]
            #print(dictArr)
    return result



def lilyHw(nums):
    nums1= nums.copy()
    asce = sorted(nums)
    desc = list(reversed(asce))
    #print(asce, nums)
    r1 = swaping(asce, nums)
    #print(desc, nums)
    r2 = swaping(desc, nums1)
    return min(r1, r2)



# Test case 1
arr1 = [7, 15, 12, 3]
print(lilyHw(arr1))

# Test case 2
arr2 = [2, 5, 3, 1]
print(lilyHw(arr2))

# Test case 3
arr3 = [15, 13, 10, 9, 8, 4, 1, 3]
print(lilyHw(arr3))

# Test case 4
arr4= [2, 3, 1]
print(lilyHw(arr4))

# Test case 5
arr5 = [3,2,1]
print(lilyHw(arr5))