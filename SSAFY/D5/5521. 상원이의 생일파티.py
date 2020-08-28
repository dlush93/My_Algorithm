for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    invited = []
    invited.extend(graph[1])
    for friend in graph[1]:
        invited.extend(graph[friend])
    result = list(set(invited))
    if 1 in result:
        print('#{} {}'.format(t, len(result)-1))
    else:
        print('#{} {}'.format(t, len(result)))