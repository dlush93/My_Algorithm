for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for i in range(M):
        node, value = map(int, input().split())
        graph[node].append(value)
    while not graph[L]:
        if N%2:
            graph[N//2].append(graph[N][0] + graph[N-1][0])
            N -= 2
        else:
            graph[N//2].append(graph[N][0])
            N -= 1
    print('#{} {}'.format(t, graph[L][0]))