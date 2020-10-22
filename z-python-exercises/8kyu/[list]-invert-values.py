'''
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.

# 1
def invert(lst):
    i = 0
    inv = []
    while i < len(lst):
        inv.append(lst[i] * -1)
        i += 1
    return inv

# 2
def invert(lst):
    lst2=[]
    for num in lst:
        lst2.append(num*-1)
    return lst2
'''


def invert(lst):
    return [-i for i in lst]


print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))
print(invert([]))
