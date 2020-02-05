for t in range(1,11):
    tc = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    result = []
    for i in range(100):
        SUM_i = 0
        SUM_j = 0
        for j in range(100):
            SUM_i += arr[i][j]
            SUM_j += arr[j][i]
        result.append(SUM_i)
        result.append(SUM_j)
    for i, j in enumerate(range(100)):
        SUM = 0
        SUM += arr[i][j]
        result.append(SUM)
        SUM = 0
        SUM += arr[i][99-j]
        result.append(SUM)
    ans = max(result)
    print('#{} {}'.format(t, ans))