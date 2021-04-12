from collections import deque
import sys


def bfs(start):
    hacking = 0
    q = deque()
    q.append(start)
    visit = [0] * (N + 1)
    visit[start] = 1
    while q:
        node = q.popleft()
        hacking += 1
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)
    return hacking


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
max_hacking = 0
result = []
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)
for i in range(1, N + 1):
    if graph[i]:
        temp = bfs(i)
        if temp > max_hacking:
            max_hacking = temp
            result = [i]
        elif temp == max_hacking:
            result.append(i)
print(*result)