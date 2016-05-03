def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        print('left[i]: {} right[j]: {}'.format(left[i],right[j]))
        if left[i] <= right[j]:
            print('Appending {} to the result'.format(left[i]))
            result.append(left[i])
            print('result now is {}'.format(result))
            i += 1
            print('i now is {}'.format(i))
        else:
            print('Appending {} to the result'.format(right[j]))
            result.append(right[j])
            print('result now is {}'.format(result))
            j += 1
            print('j now is {}'.format(j))
    print('One of the list is exhausted. Adding the rest of one of the lists.')
    result += left[i:]
    result += right[j:]
    print('result now is {}'.format(result))
    return result

def mergesort(L):
    print('---')
    print('mergesort on {}'.format(L))
    if len(L) < 2:
        print('length is 1: returning the list without changing')
        return L
    middle = len(L) / 2
    print('calling mergesort on {}'.format(L[:middle]))
    left = mergesort(L[:middle])
    print('calling mergesort on {}'.format(L[middle:]))
    right = mergesort(L[middle:])
    print('Merging left: {} and right: {}'.format(left,right))
    out = merge(left, right)
    print('exiting mergesort on {}'.format(L))
    print('#---')
    return out


print mergesort([6,5,4,3,2,1,7,8,9,10])
