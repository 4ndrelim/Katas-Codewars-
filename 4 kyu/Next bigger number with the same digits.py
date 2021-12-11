# Description #

# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071

# Note: If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil


def next_bigger(n):
    split = list(str(n))
    l = len(split)
    index = None
    for i in range(l-1):
        if int(split[l-1-i-1]) < int(split[l-1-i]):
            index = l-1-i
            break
    else:
        return -1
    t = int(split[index-1])
    minIdx = l-1
    while int(split[minIdx]) <= t: #find index of the 1st/smallest number thats bigger than t
        minIdx -= 1
    split[index-1], split[minIdx] = split[minIdx], split[index-1]
    res = split[:index] + sorted(split[index:])
    return int(''.join(res))
