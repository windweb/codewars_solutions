words = ['hello', 'world', 'this', 'is', 'great']


def smash(words):
    result = ""
    for index in range(len(words)):
        if index != len(words)-1:
            result = result + words[index] + " "
        else:
            result = result + words[index]
    return result


smash(words)
