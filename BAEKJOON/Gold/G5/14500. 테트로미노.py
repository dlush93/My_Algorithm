def tetromino(arr, cnt):
    global result
    if cnt == 4:
        result = max(result, sum([board[a[0]][a[1]] for a in arr]))
        return

    for i in range(4):
        x, y = arr[-1][0] + dx[i], arr[-1][1] + dy[i]
        if 0 <= x < N and 0 <= y < M:
            if visited[x][y] == 0:
                visited[x][y] = 1
                arr.append([x, y])
                tetromino(arr, cnt+1)
                arr.pop()
                visited[x][y] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
result = 0
T_shape = [[[0, 1], [0, 2], [1, 1]], [[0, 1], [0, 2], [-1, 1]], [[1, 0], [2, 0], [1, 1]], [[1, 0], [2, 0], [1, -1]]]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        tetromino([[i, j]], 1)
        visited[i][j] = 0
        for T in T_shape:
            temp = board[i][j]
            for t in T:
                x, y = i+t[0], j+t[1]
                if 0 <= x < N and 0 <= y < M:
                    temp += board[x][y]
                else:
                    break
            result = max(result, temp)
print(result)