for t in range(1,11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    data = [[arr[i*2], arr[i*2+1]] for i in range(E)]
    graph = [[0]*(V+1) for i in range(V+1)]
    a = V
    for d in data:
        graph[d[1]][d[0]] = 1
    stack = []
    for j in range(1,V+1):
        if 1 not in graph[j]:
            work = j
            stack.append(work)
            break
    while a != 0:
        a -=1
        for k in range(1, V+1):
            graph[k][work] = 0
        for l in range(1, V+1):
            if 1 not in graph[l] and l not in stack:
                work = l
                stack.append(work)
                break
    print('#{} {}'.format(t, ' '.join(map(str, stack))))