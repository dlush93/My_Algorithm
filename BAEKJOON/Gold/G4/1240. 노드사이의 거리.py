from collections import deque

def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited[start] = 0
    min_dis = 100000000000

    while q:
        now_node, now_dis = q.popleft()
        for next_node, dist in distance[now_node]:
            if next_node == end:
                min_dis = min(min_dis, now_dis + dist)
            if visited[next_node]:
                visited[next_node] = 0
                q.append((next_node, now_dis + dist))

    return min_dis

N, M = map(int, input().split())
distance = dict()
for i in range(N-1):
    node1, node2, dis = map(int, input().split())
    if node1 not in distance:
        distance[node1] = []
    if node2 not in distance:
        distance[node2] = []
    distance[node1].append((node2, dis))
    distance[node2].append((node1, dis))

for i in range(M):
    s, e = map(int, input().split())
    visited = [1 for _ in range(N+1)]
    print(bfs(s, e))