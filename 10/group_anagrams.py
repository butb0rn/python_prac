'''
Write a method to sort an array of strings so that all the anagrams
are next to each other.
'''

def sort_anagrams(alist):
    if alist:
        result = []
        map_list = {}

        for item in alist:
            anagram_key = sort_key(item)
            if anagram_key in map_list:
                map_list[anagram_key].append(item)
            else:
                map_list[anagram_key] = [item]

        for key in map_list.keys():
            temp = map_list[key]
            for value in temp:
                result.append(value)

        return result

def sort_key(item):
    if item:
        return ''.join(sorted(item))

alist = ['abc', 'gfh', 'cab', 'ab', 'gggg', 'gggf', 'fph']
print sort_anagrams(alist)
