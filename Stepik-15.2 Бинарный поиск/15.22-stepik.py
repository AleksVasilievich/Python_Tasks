# Линейный поиск

def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

print(LinearSearch([1,2,3,4,5,2,1], 2))





# Бинарный поиск

def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == - 1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

lys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val = 5
print(BinarySearch(lys, val))
print(BinarySearch([1, 2, 3, 4, 5], 2))


# Jump Search

import math

def JumpSearch (lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1

print(JumpSearch([1,2,3,4,5,6,7,8,9], 5))