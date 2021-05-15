# Question- we have two array(arr and brr) and we have to find all the numbers which present in brr but not in arr.
# If frequency of the number also differ then it also count in missing number
def missingnum(ar, br):
    A, B= ar, br
    position= 0
    while position < (len(br)-1):
        target= br[position]
        print(target)
        output= bsearch(ar, target)
        print('output:', output)
        if output == -1:
            position += 1
        else:
            B.remove(output)
    return B

def missing_num(ar, br):
    missing= set()
    for n in br:
        if n in ar:
            ar.remove(n)
        else:
            missing.add(n)
    return sorted(list(missing))


size_arr= 10
size_brr= 13
arr= [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr= [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
result= missing_num(arr, brr)
print(result)

