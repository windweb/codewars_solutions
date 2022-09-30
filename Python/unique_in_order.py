iterable = 'AAAABBBCCDAABBB'
# iterable = 'ABBCcAD'
# iterable = [1,2,2,3,3]


def unique_in_order(iterable):
    previous_item = ""
    result = []
    for item in iterable:
        if item != previous_item:
            result.append(item)
        previous_item = item
    print(result)


unique_in_order(iterable)