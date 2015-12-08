__author__ = 'butb0rn'

'''
Write a method to return all subsets of a set.
'''

def sub_reader(aset):
    helper_set = []
    index = -1
    print sub_creator(aset, helper_set, index)

def sub_creator(aset, helper_set, index):

    if (len(helper_set) == 0):
        helper_set.append([])
    else:
        item = aset[index]
        more_subsets = []
        for subset in helper_set:
            new_subset = []
            new_subset.extend(subset)
            new_subset.append(item)
            more_subsets.append(new_subset)

        helper_set.extend(more_subsets)
    if index+1 < len(aset):
        sub_creator(aset, helper_set, index + 1)

    return helper_set

aset = ['a1', 'a2', 'a3']
sub_reader(aset)
