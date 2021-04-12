for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    result = b
    for j in range(a, 1, -1):
        if result == j:
            break
        while result%j == 0:
            result //= j
        else:
            if result == 1:
                a = b
    print(a*result)