from collections import deque

def move(nb, d):
    can_sum = [[True]*N for i in range(N)]

    if d == 0 or d == 1:
        start, end, step = N-1, -1, -1
    else:
        start, end, step = 0, N, 1

    for i in range(start, end, step):
        for j in range(start, end, step):
            if not nb[i][j]:
                x, y = i, j
                nx, ny = i + dx[d], j + dy[d]
                value = nb[i][j]
                nb[i][j] = 0
                while True:
                    if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                        break
                    if nb[nx][ny] == 0:
                        nx += dx[d]
                        ny += dy[d]
                    elif nb[nx][ny] == value and can_sum[nx][ny]:
                        x, y = nx, ny
                        can_sum[x][y] = False
                        break
                    else:
                        break
                nb[x][y] += value





N = int(input())
B = [list(map(int, input().split())) for i in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]