from collections import deque
import sys
input = sys.stdin.readline
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
front_dis = [[1000000]*M for _ in range(N)]
end_dis = [[1000000]*M for _ in range(N)]
front_dis[0][0] = 1
end_dis[N-1][M-1] = 0
front_q = deque()
end_q = deque()
front_q.append([0, 0, 1])
end_q.append([N-1, M-1, 0])
while front_q:
    x, y, dis = front_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if front_dis[nx][ny] == 1000000:
                front_dis[nx][ny] = dis + 1
                if arr[nx][ny] == '0':
                    front_q.append([nx, ny, dis + 1])

while end_q:
    x, y, dis = end_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if end_dis[nx][ny] == 1000000:
                end_dis[nx][ny] = dis + 1
                if arr[nx][ny] == '0':
                    end_q.append([nx, ny, dis + 1])

result = front_dis[N-1][M-1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            result = min(result, front_dis[i][j] + end_dis[i][j])

if result == 1000000:
    print(-1)
else:
    print(result)