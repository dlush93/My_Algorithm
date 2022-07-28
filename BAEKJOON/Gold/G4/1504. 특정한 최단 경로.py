import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    distance = [float('inf') for _ in range(N)]
    distance[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while q:
        current_dist, current_node = heapq.heappop(q)
        if current_dist > distance[current_node]:
            continue

        for dist, next_node in graph[current_node]:
            whole_dist = dist + current_dist
            if whole_dist < distance[next_node]:
                distance[next_node] = whole_dist
                heapq.heappush(q, [whole_dist, next_node])
    return distance


N, E = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s-1].append([d, e-1])
    graph[e-1].append([d, s-1])
v1, v2 = map(int, input().split())
start = min(dijkstra(0)[v1-1], dijkstra(0)[v2-1])
mid = dijkstra(v1-1)[v2-1]
end = min(dijkstra(v1-1)[N-1], dijkstra(v2-1)[N-1])
print(start+mid+end)