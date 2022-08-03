from collections import deque

def dfs(s):
    q = deque()
    q.append([s, 0])
    visited[s] = 1
    while q:
        x, cnt = q.popleft()
        for i in group[x]:
            if visited[i] == 0:
                visited[i] = 1
                if i == end:
                    return cnt + 1
                else:
                    q.append([i, cnt + 1])
    return -1


n = int(input())
start, end = map(int, input().split())
m = int(input())
group = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    group[x].append(y)
    group[y].append(x)
print(dfs(start))