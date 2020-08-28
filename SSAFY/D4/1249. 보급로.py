from collections import deque
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0<= nx < N:
                if arr[ny][nx] > arr[y][x] + data[y][x]:
                    arr[ny][nx] = arr[y][x] + data[y][x]
                    q.append([ny,nx])

for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, list(input()))) for i in range(N)]
    arr = [[10000000]*N for i in range(N)]
    arr[0][0] = 0
    bfs([0,0])
    print('#{} {}'.format(t, arr[-1][-1]))