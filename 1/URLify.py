def urlify(sen, len_sen):
    sen = list(sen)
    for i in range(len_sen):
        if sen[i] == ' ':
            sen[i] = '%20'
    print ''.join(sen[:len_sen])

urlify("Mr john smith    ",13)
