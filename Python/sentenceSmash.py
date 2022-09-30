words = ['hello', 'world', 'this', 'is', 'great']


def smash(words):
    result = ""
    for i in range(len(words)):
        if i != len(words)-1:
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return print(result)


smash(words)
