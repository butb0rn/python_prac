def is_unique(input):

    if not input:
        raise NameError('Empty input')
    input = input.lower()
    char_key = {}
    for i in input:
        if i in char_key.keys():
            char_key[i] += 1
            print False
            return
        else:
            char_key[i] = 1
    print True


is_unique("Ehsan")
is_unique("EhSEs")
