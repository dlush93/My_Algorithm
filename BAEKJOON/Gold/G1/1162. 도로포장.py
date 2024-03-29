import heapq


def dijkstra(start):
    distance = [[float('inf') for _ in range(N)] for _ in range(2)]
    q = []
    distance[0][start] = 0
    heapq.heappush(q, [distance[0][start], start, K])

    while q:
        current_dist, next_node, cnt = heapq.heappop(q)

        if distance[0][next_node] < current_dist:
            continue

        for dist, node in graph[next_node]:
            whole_dist = current_dist + dist

            if cnt > 0 and current_dist < distance[]:

            if whole_dist < distance[node]:
                distance[node] = whole_dist
                heapq.heappush(q, [whole_dist, node])


    return distance


N, M, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s-1].append([c, e-1])
    graph[e-1].append([c, s-1])
print(dijkstra(0))
