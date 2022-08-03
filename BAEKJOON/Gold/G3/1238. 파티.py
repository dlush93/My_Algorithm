import heapq


def dijkstra(start):
    q = []
    dist = [float('inf') for _ in range(N)]
    heapq.heappush(q, [0, start])
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next_node, next_d in graph[now]:
            whole_dist = d + next_d
            if whole_dist < dist[next_node]:
                dist[next_node] = whole_dist
                heapq.heappush(q, [whole_dist, next_node])
    return dist


N, M, X = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s-1].append([e-1, d])
max_dist = 0
for i in range(N):
    go, back = dijkstra(i), dijkstra(X-1)
    max_dist = max(max_dist, go[X-1] + back[i])
print(max_dist)