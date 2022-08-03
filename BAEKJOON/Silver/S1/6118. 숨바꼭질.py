from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([barn[1], 0])
    while q:
        way, cnt = q.popleft()
        for w in way:
            if visited[w] == 0:
                visited[w] = 1
                q.append([barn[w], cnt+1])
                if cnt+1 not in length:
                    length[cnt+1] = []
                length[cnt+1].append(w)



N, M = map(int, input().split())
barn = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    barn[a].append(b)
    barn[b].append(a)
length = dict()
visited = [0 for _ in range(N+1)]
visited[1] = 1
bfs()
max_value = max(length)
print(f'{min(length[max_value])} {max_value} {len(length[max_value])}')