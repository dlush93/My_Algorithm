test = int(input())
a = list(range(10))
for t in range(1, test+1):
    N = int(input())
    arr = []
    i=0
    while arr != a:
        i += 1
        b = str(N*i)
        c = len(b)
        for j in range(c):
            if int(b[j]) not in arr:
                arr.append(int(b[j]))
            arr.sort()
    print('#{} {}'.format(t, N*i))
