for t in range(1,11):
    input()
    data = [list(input()) for x in range(100)]
    cnt = 0
    for i in range(100):
        for j in range(100):
            for n in range(100-j,0,-1):
                x = data[i][j:j+n]
                if x == x[::-1]:
                    cnt = max(len(x),cnt)
                y = [data[j+dy][i] for dy in range(n)]
                if y == y[::-1]:
                    cnt = max(len(y),cnt)
    print('#{} {}'.format(t, cnt))