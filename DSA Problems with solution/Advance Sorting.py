def mergesort(cards):
    if len(cards) <= 1:
        return cards

    mid= len(cards) // 2
    left= cards[:mid]
    right= cards[mid:]
    left_sorted= mergesort(left)
    right_sorted= mergesort(right)
    sorted_list= merge(left_sorted, right_sorted)

    return sorted_list


def merge(num1, num2):
    sorted_nums= []
    i,j,k = 0,0,0

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            sorted_nums.append(num1[i])
            i += 1
        elif num1[i] > num2[j]:
            sorted_nums.append(num2[j])
            j += 1
        k += 1

    left_tail, right_tail= num1[i:], num2[j:]

    return sorted_nums + left_tail + right_tail


def quicksort(cards, start= 0, end=None):
    if end is None:
        end= len(cards)-1
    if start < end:
        pivot= parition(cards, start, end)
        quicksort(cards, start, pivot-1)
        quicksort(cards, pivot+1, end)

    return cards


def parition(cards, start= 0, end= None):
    if end is None:
        end= len(cards)-1

    l, r= start, end-1
    while l < r:

        if cards[l] <= cards[end]:
            l += 1
        elif cards[r] > cards[end]:
            r -= 1
        else:
            cards[l], cards[r]= cards[r], cards[l]

    if cards[l] > cards[end]:
        cards[l], cards[end]= cards[end], cards[l]
        return l
    else:
        return end


def shellsort():
    pass

cards= [98,69,5,2,3,8,17,23,56]
print('Before sorting: ', cards)
print('After Sorting:', quicksort(cards))





# Time complexity of merge sort O(n logn)
# Time complexity of quick sort O(n logn) for the average case O(n^2) for the worst case
