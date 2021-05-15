# This function is to apply binary search in normal manner
def binarysearch(cards, query):
    lo, hi= 0, len(cards)-1
    while(lo<=hi):

        mid= (lo+hi) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            lo= mid+1
        else:
            hi= mid-1
    return -1

# This function to apply binary serach in recursive manner
def binaryserachrec(lo, hi, condition):

    while(lo <= hi):
        mid = (lo+hi) // 2
        result= condition(mid)
        if result == 'found':
            return mid
        elif result == 'right':
            lo= mid+1
        else:
            hi= mid-1
    return -1

def locate_element(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'right'
        else:
            return 'left'

    return binaryserachrec(0, len(cards)-1, condition)



cards= list(map(int, input('Enter the cards elements: ').split()))
cards.sort()
query= int(input('Enter the element you want to serach in the cards: '))

output= locate_element(cards, query)       # Uncomment this command to perform binary search with recursion
                                           # (if you are uncommenting the comment below command)

#output= binarysearch(cards, query)       # Uncomment this command to perform binary search without recursion
                                          # (if you are uncommenting the comment above command)

if output == -1:
    print('Element for which you are searching for is NOT FOUND')
else:
    print('Element is Found at position: ', output)