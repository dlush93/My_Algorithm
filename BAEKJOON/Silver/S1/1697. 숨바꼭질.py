from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == M:
            return lotation[x]
        for i in range(3):
            if i == 0:
                nx = x -1
            elif i == 1:
                nx = x + 1
            else:
                nx = 2*x
            if 0 <= nx <= 100000 and lotation[nx] == -1:
                lotation[nx] = lotation[x] + 1
                q.append(nx)


N, M = map(int, input().split())
lotation = [-1]*100001
lotation[N] = 0
print(bfs(N))