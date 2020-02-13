for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    arr = [[] for i in range(V+1)]
    for i in range(1,E+1):
        a,b = map(int, input().split())
        arr[a] += [b]
    S, G = map(int, input().split())
    for i in arr[S]:
        arr[S] += arr[i]
    if G in arr[S]:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))