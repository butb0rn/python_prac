def str_com(exp):
    res = [exp[0],1]
    for i in exp:
        if i == res[-2]:
            res[-1] += 1
        else:
            res.append(i)
            res.append(1)

    final_res = ''.join(map(str, res))
    print final_res if len(final_res) < len(exp) else exp
    


str_com("aabbcccccaaa")
