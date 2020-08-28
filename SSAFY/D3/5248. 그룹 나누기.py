for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    visit = [0]*(N+1)
    graph = [[0]*(N+1) for i in range(N+1)]
    for i in range(M):
        graph[data[i*2]][data[i*2+1]] += 1
        graph[data[i*2+1]][data[i*2]] += 1
    result = []
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 1:
                cnt += 1
        result.append(cnt)
        cnt = 0
    if N < sum(result)//2:
        print('#{} 1'.format(t))
    else:
        print('#{} {}'.format(t, N - sum(result)//2))
