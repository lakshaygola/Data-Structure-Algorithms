# Function to perform bubble sort on the given list
def bubble_sort(cards):
    for _ in range(len(cards)-1):                                        # Executing for n-1 times
        for num in range(len(cards)-1):                                  # Executing for n-1 times
            if cards[num] > cards[num+1]:
                cards[num+1], cards[num]= cards[num], cards[num+1]

    return cards

# Function to implement the insertion sort of the given numbers
def insertion_sort(cards):
    for i in range(len(cards)):
        for j in range(len(cards)-1):
            if cards[j] > cards[j+1]:
                cards[j], cards[j+1] = cards[j+1], cards[j]
                j += 1
            else:
                j += 1
    return cards


cards= [98,69,5,2,3,8,17,23,56]
size= len(cards)
print('Unsorted list: ', cards)
print('Sorted list: ', bubble_sort(cards))
print(insertion_sort(cards) == bubble_sort(cards))


# Total complixity of the bubble sort will be O(n^2)
# Total complixity of the insertion sort will be O(n^2)
