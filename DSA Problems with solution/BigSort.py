"""Problem Statement:- We have a list or array containing numeric integer in the form of string.We have to sort them."""

# Helper function (perform merge operation on two list)
def merge(left, right):
    lp, rp = 0, 0
    sorted = []
    while lp < len(left) and rp < len(right):

        if left[lp] <= right[rp]:
            sorted.append(left[lp])
            lp += 1
        else:
            sorted.append(right[rp])
            rp += 1

    return sorted + left[lp:] + right[rp:]


# Function to solve the problem (recursively)
def bigSort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]
    print('Left: ', left, 'Right: ', right)
    left_sort, right_sort = bigSort(left), bigSort(right)
    sorted = merge(left_sort, right_sort)
    return sorted




# Test Case 1
unsorted1 = ['6', '31415926535897932384626433832795', '1', '3', '10', '3', '5']
unsorted1 = list(map(int, unsorted1))
print(bigSort(unsorted1))