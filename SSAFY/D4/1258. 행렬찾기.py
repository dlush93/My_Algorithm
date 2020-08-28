for t in range(1, int(input())+1):
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]
    arr = [[0]*n for i in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and data[i][j] != 0:
                y1, x1 = i, j
                for k in range(i, n):
                    if data[k][j] == 0:
                        y2 = k-1
                        break
                    else:
                        y2 = k
                for l in range(j, n):
                    if data[i][l] == 0:
                        x2 = l-1
                        break
                    else:
                        x2 = l
                for a in range(y1, y2+1):
                    for b in range(x1, x2+1):
                        arr[a][b] = 1
                result.append([y2-y1+1, x2-x1+1])
    num = len(result)
    for i in range(num):
        result[i].insert(0, result[i][0]*result[i][-1])
    print('#{} {} '.format(t, num), end='')
    for i in sorted(result):
        print('{} {} '.format(i[1], i[2]), end='')
    print()