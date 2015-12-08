'''
You are given an array-like data structure Listy(I fake the Listy with simple list and -1 is the last item)
which lacks a size method. It does, however, have an elementAt(i) method that returns the element at index i in
structure only supports postitive integers. Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. if x occurs multiple times, you may return any index.
'''
def sorted_search(alist, value):
    index = 1
    #find length of the array.
    while (alist[index] != -1) and (alist[index] < value):
        index *= 2

    return binary_search(alist, value, index / 2, index)

def binary_search(alist, value, low, high):
    middle_element = 0
    while (low <= high):
        mid = (low + high) / 2
        middle_element = alist[mid]
        if (middle_element > value) or (middle_element == -1):
            high = mid - 1
        elif middle_element < value:
            low = mid + 1
        else:
            return mid

    return -1

alist = [2, 4, 5, 8, 9, 12, 15, 19, -1]
print sorted_search(alist, 19)
