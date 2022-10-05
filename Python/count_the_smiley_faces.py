def count_smileys(arr):
    count_smile = 0
    for item in arr:
        if len(item) == 3:
            if ((item[0] == ':' or item[0] == ';') and
               (item[1] == '-' or item[1] == '~') and
               (item[2] == ')' or item[2] == 'D')):
                count_smile += 1
        elif len(item) == 2:
            if ((item[0] == ':' or item[0] == ';') and
                (item[1] == ')' or item[1] == 'D')):
                count_smile += 1
        else:
            count_smile += 0
    print(count_smile)


count_smileys([])  # 0
count_smileys([':D',':~)',';~D',':)'])  # 4
count_smileys([':)',':(',':D',':O',':;'])  # 2
count_smileys([';]', ':[', ';*', ':$', ';-D'])  # 1
