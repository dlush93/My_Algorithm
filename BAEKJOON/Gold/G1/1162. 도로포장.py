N, M, K = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
