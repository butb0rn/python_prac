def merge_list(a, b, lastA, lastB):
    index_a = lastA
    index_b = lastB
    index_merged = len(a) - 1

    while(index_b >= 0):
        if(index_a >= 0 and a[index_a] > b[index_b]):
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1

        index_merged -= 1

    return a



a = [1, 4, 6, 14, None, None, None, None, None]
b = [2, 5, 9, 10, 16]
print merge_list(a, b, 4, 5)
