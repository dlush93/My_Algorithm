for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = [list(input()) for x in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            x = data[i][j:j+M]
            if x == x[::-1]:
                print('#{} {}'.format(t, ''.join(x)))
                break
            y = [data[j+y][i] for y in range(M)]
            if y == y[::-1]:
                print('#{} {}'.format(t, ''.join(y)))
                break