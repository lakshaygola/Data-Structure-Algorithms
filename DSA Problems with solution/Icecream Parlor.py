""" Two friend went to the ice cream parlor, parlor have different flavour at different price we have to write the
    function In which two friend choose different flavour of ice cream such that total price of the ice cream will
    be equal to the total price pool by both friends"""

# Binary search function to find the solution of the problem
def binarysearch(data, target):
    data.sort()
    lo, hi= 0, len(data)-1
    while lo <= hi:
        mid= (lo + hi) // 2

        if data[mid] == target:
            return mid
        if target < data[mid]:
            hi= mid-1
        else:
            lo= mid+1
    return 0


def icecream_flavours(cards, target):
    i, j = 0, len(cards) - 1
    flavours = []
    while i < len(cards):
        while i < j:
            if cards[i] + cards[j] == target:
                flavours.append(i+1)
                flavours.append(j+1)
                return flavours
            else:
                j -= 1
        i += 1
        j= len(cards)-1
    return flavours
# Time complexity of this solution is O(n^2)

def effIcecream(card, target):
    data= card
    for position in range(len(data)):
        data.sort()
        current= data.pop(position)
        #print('current: ', current)
        comp= target - current
        #print('data : ',data)
        #print('complement: ', comp)
        idx= binarysearch(data, comp)
        #print('idx: ', idx)
        if idx:
            return [position+1, idx+2]
        data.append(current)


money, n = 8, 6
price = [1 ,2]
result = effIcecream(price, money)
print(result)
