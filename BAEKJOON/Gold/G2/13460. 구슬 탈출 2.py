from collections import deque


def init_ball():
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            if B[i][j] == 'B':
                bx, by = i, j
    q.append([rx, ry, bx, by, 1])
    visited[rx][ry][bx][by] = False


def tilt(x, y, mx, my):
    distance = 0
    while B[x+mx][y+my] != '#' and B[x][y] != 'O':
        x += mx
        y += my
        distance += 1
    return x, y, distance


def bfs():

    init_ball()

    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            break
        for i in range(4):
            now_rx, now_ry, r_distance = tilt(rx, ry, dx[i], dy[i])
            now_bx, now_by, b_distance = tilt(bx, by, dx[i], dy[i])
            if B[now_bx][now_by] != 'O':
                if B[now_rx][now_ry] == 'O':
                    print(cnt)
                    return
                if now_rx == now_bx and now_ry == now_by:
                    if r_distance > b_distance:
                        now_rx -= dx[i]
                        now_ry -= dy[i]
                    else:
                        now_bx -= dx[i]
                        now_by -= dy[i]
                if visited[now_rx][now_ry][now_bx][now_by]:
                    visited[now_rx][now_ry][now_bx][now_by] = False
                    q.append([now_rx, now_ry, now_bx, now_by, cnt+1])
    print(-1)


N, M = map(int, input().split())
B = [list(input()) for i in range(N)]
visited = [[[[True]*M for i in range(N)] for j in range(M)] for k in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
bfs()