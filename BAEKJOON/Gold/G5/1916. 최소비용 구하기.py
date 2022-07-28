import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    distance = [float('inf') for _ in range(N)]
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        current_dist, next_node = heapq.heappop(q)
        if current_dist > distance[next_node]:
            continue

        for dist, node in graph[next_node]:
            whole_dist = current_dist + dist
            if whole_dist < distance[node]:
                distance[node] = whole_dist
                heapq.heappush(q, [whole_dist, node])

    return distance


N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s-1].append([c, e-1])
S, E = map(int, input().split())
print(dijkstra(S-1)[E-1])