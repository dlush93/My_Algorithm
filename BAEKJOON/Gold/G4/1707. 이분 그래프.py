import sys
input = sys.stdin.readline

for t in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(graph)