def samsubstrings(number):
    total = 0
    for idx in range(len(number)):
        for j in range(1, len(number)):
            sub = int(number[idx:j])
            total += sub
    return total

nums= '16'
print(samsubstrings(nums))