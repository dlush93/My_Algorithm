def DFS(start):
    global temp, result, final_result

    if len(temp) == N-1:
        for i, j in temp:
            result += data[i][j]

        result += data[start][0]
        final_result.append(result)
        result = 0
        return

    for i in range(1, N):
        if not visit[i]:
            temp.append((start, i))
            visit[i] = True
            DFS(i)
            temp.remove((start, i))
            visit[i] = False


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    visit = [0] * N
    temp = []
    result = 0
    final_result =[]
    DFS(0)

    print('#{} {}'.format(t, min(final_result)))