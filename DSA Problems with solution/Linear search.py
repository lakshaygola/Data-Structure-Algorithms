# Defining the function to perform the linear search on the given number
def linearserach(cards, query):
    position= 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position +=1
    return -1
# This function perform the linear serach but recursivly
def linearrec(cards, query, start):
    if start < len(cards):
        if cards[start] == query:
            return start
    return linearrec(cards, query, start+1)


cards= list(map(int, input('Enter the cards elements: ').split()))
cards.sort()
query= int(input('Enter the element you are searching for: '))
position=0
output= linearrec(cards, query, position)

if output == -1:
    print('Element you are searching for is Not Found')
else:
    print('Element for which you are searching for in found at position: ', output)