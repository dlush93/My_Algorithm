def dfs(node, cnt):
    stack =[]
    stack.append(node)

    while stack:
        x = stack.pop()
        for i in graph[x]:
            stack.append(i)
            cnt +=1
    return cnt


for t in range(1, int(input())+1):
    E, N = map(int, input().split())
    graph = [[] for i in range(E+2)]
    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i+1])
    result = dfs(N, 1)
    print('#{} {}'.format(t, result))
