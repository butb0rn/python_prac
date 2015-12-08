'''
Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.
'''
def sparse_search(alist, value):
    if alist:
        return search(alist, value, 0, len(alist) - 1)
    else:
        return -1


def search(alist, value, low, high):
    if low > high:
        return -1

    mid = (low + high) / 2
    if alist[mid] == '':
        left = mid - 1
        right = mid + 1
        while (True):
            if (left < low) and (right > high):
                return -1
            elif (right <= high) and (alist[right] != ''):
                mid = right
                break
            elif (left >= low) and (alist[left] != ''):
                mid = left
                break
            left -= 1
            right += 1
    if alist[mid] == value:
        return mid
    elif alist[mid] < value:
        return search(alist, value, mid + 1, high)
    else:
        return search(alist, value, low, mid - 1)

alist = ['aaa', '', 'bbb', '', 'eee', '', 'hhh', 'nnn', '', '', 'sss', '', '']
print sparse_search(alist, 'eee')
