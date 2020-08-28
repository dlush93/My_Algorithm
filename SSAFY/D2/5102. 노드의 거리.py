def bfs(S, G):
    stack = []
    visit = [0]*(V+1)
    stack.append((S, 0))
    visit[S] = 1
    while stack:
        s, cnt = stack.pop(0)
        for i in arr[s]:
            if i == G:
                return cnt + 1
            elif visit[i] ==0:
                visit[i] = 1
                stack.append((i, cnt+1))
    return 0

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[0] for i in range(V+1)]
    for i in range(E):
        y, x = map(int, input().split())
        arr[y].append(x)
        arr[x].append(y)
    S, G = map(int, input().split())
    result = bfs(S,G)
    print('#{} {}'.format(t, result))