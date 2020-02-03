di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    res = 0
    tmp = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            k=arr[i][j]
            SUM = 0
            for x in range(4):
                dx = i + di[x]
                dy = j + dj[x]
                if 0<=dx<N and 0<=dy<N:
                    SUM +=abs(k-arr[dx][dy])
            tmp[i][j] = SUM
    print('#{} {}'.format(tc,res))