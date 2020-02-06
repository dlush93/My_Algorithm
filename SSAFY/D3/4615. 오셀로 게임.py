test = int(input())
for t in range(1, test+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(M)]
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    arr = [[0]*N for i in range(N)]
    arr[N-2][N-2], arr[N-1][N-2], arr[N-2][N-1], arr[N-1][N-2] = 100, 1, 1, 100
    for d in data:
        if d[2] ==1:
            arr[d[0]][d[1]] = 1
            for i in range(8):
                a = 1
                if 0 <= d[0]+dx[i] < N and 0 <= d[0]+dx[i] < N:
                    if arr[d[0]+dx[i]][d[1]+dy[i]] == 100:
                        while arr[d[0]+dx[i]*a][d[1]+dy[i]*a] == 100:
                            if 0 <= d[0] + dx[i]*a < N and 0 <= d[0] + dx[i] < N:
                                a +=1
                        if arr[d[0]+dx[i]*a][d[1]+dy[i]*a] != 100:
                            for j in range(a - 1):
                                arr[d[0] + dx[i] * j][d[1] + dy[i] * j] = 1
        else:
            arr[d[0]][d[1]] = 100
            for i in range(8):
                a = 1
                if 0 <= d[0] + dx[i] < N and 0 <= d[0] + dx[i] < N:
                    if arr[d[0] + dx[i]][d[1] + dy[i]] == 1:
                        while arr[d[0] + dx[i] * a][d[1] + dy[i] * a] == 1:
                            if 0 <= d[0] + dx[i] * a < N and 0 <= d[0] + dx[i] < N:
                                a += 1
                        if arr[d[0] + dx[i] * a][d[1] + dy[i] * a] != 1:
                            for j in range(a - 1):
                                arr[d[0] + dx[i] * j][d[1] + dy[i] * j] = 100
    result = 0
    for k in arr:
        result += sum(k)
    print('#{} {} {}'.foramt(t, result%100, result//100))