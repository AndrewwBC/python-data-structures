sortedList = [2, 4, 5, 7, 8, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37, 57]

def binarySearch(data, target, low, high):
    
    mid = (low + high) // 2

    print(data[mid], data[low:high],target, low, high)

    if low > high:
        return False
    else:
        if target == data[mid]:
            return target
    
        elif target < data[mid]:
            return binarySearch(sortedList, target, low, mid - 1)
        else:
            return binarySearch(sortedList, target, mid + 1, high)

result = binarySearch(sortedList, 57, 0, 16)
print(result)

def reverse(S, start, stop):
    print(S)
    if start < stop - 1: # if at least 2 elements:
        S[start], S[stop - 1] = S[stop -1], S[start] # swap first and last
        reverse(S, start + 1, stop- 1)
        
listToReverse = [1,2,3,4,5]

print(reverse(listToReverse, 0, len(listToReverse)))