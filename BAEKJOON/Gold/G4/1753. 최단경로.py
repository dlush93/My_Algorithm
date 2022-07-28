import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    distance = [float('inf') for _ in range(V)]
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        current_dist, next_node = heapq.heappop(q)
        if current_dist > distance[next_node]:
            continue

        for dist, node in graph[next_node]:
            whole_dist = dist + current_dist
            if whole_dist < distance[node]:
                distance[node] = whole_dist
                heapq.heappush(q, [whole_dist, node])

    return distance


V, E = map(int, input().split())
S = int(input())-1
graph = [[] for _ in range(V)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s-1].append([d, e-1])
for d in dijkstra(S):
    if d == float('inf'):
        print('INF')
    else:
        print(d)