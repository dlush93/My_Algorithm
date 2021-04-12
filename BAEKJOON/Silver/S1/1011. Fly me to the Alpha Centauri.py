for t in range(int(input())):
    x, y = map(int, input().split())
    distance = y - x
    n = 0
    time = 0
    while True:
        if n**2 >= distance:
            break
        else:
            n += 1
    if distance > n*(n-1):
        time = 2*n - 1
    else:
        time = 2*(n-1)
    print(time)