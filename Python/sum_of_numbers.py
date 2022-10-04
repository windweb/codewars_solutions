def get_sum(a,b):
    result = []
    if a == b:
        print(a)  # print() --> return
    elif a < b:
        for num in range(a, b+1, 1):
            result.append(num)
    elif a > b:
        for num in range(a, b-1, -1):
            result.append(num)
    print(sum(result))  # print() --> return


# get_sum(0,1)  # 1
get_sum(0,-1)  # -1
