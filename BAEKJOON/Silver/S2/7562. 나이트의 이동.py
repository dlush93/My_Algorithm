from collections import deque
dx, dy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x, y, cnt = q.popleft()
        if x == end[0] and y == end[1]:
            return cnt

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if arr[nx][ny] == -1:
                    arr[nx][ny] = cnt + 1
                    q.append([nx, ny, cnt + 1])

    return cnt


for t in range(int(input())):
    l = int(input())
    start = list(map(int, input().split())) + [0]
    end = list(map(int, input().split()))
    arr = [[-1]*l for i in range(l)]
    print(bfs(start))