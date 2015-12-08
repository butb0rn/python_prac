__author__ = 'butb0rn'

'''
A magic index in an array A[0..n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers write a method to find a magic index,
if one exists, in array A.
'''

def magic_index(alist):
    print magic_fast(alist, 0, len(alist) - 1)



def magic_fast(alist, start, end):
    if end < start:
        return -1

    mid_index = (start + end) / 2
    mid_value = alist[mid_index]

    if (mid_value == mid_index):
        return mid_index

    #search left
    #left_index = min(mid_index - 1, mid_value)
    left = magic_fast(alist, start, mid_index - 1)
    if (left >= 0):
        return left


    #search right
    #right_index = max(mid_index + 1, mid_value)
    right = magic_fast(alist, mid_index + 1, end)
    return right


alist = [-10, -5, 1, 2, 2, 3, 4, 8, 8, 9, 12, 13]
magic_index(alist)