def paperwork(n, m):
    if n < 0 or m < 0:
        print(0)
    else:
        print(abs(n * m))


paperwork(5, 5)
paperwork(-5, 5)
paperwork(5, -5)
paperwork(-5, -5)
paperwork(5, 0)