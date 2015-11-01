def isUnique(input):

    if not input:
        raise NameError('Empty input')
    input = input.lower()
    charKey = {}
    for i in input:
        if i in charKey.keys():
            charKey[i] += 1
            print False
            return
        else:
            charKey[i] = 1
    print True


isUnique("Ehsan")
isUnique("EhSEs")
