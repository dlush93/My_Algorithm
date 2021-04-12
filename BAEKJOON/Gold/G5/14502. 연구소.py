from collections import deque
import copy


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0


def bfs():
    global safe
    copy_arr = copy.deepcopy(arr)
    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if copy_arr[nx][ny] == 0:
                    copy_arr[nx][ny] = 2
                    virus.append([nx, ny])
    cnt = 0
    for i in copy_arr:
        cnt += i.count(0)
    safe = max(safe, cnt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
virus = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append([i,j])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
safe = 0
wall(0)
print(safe)
