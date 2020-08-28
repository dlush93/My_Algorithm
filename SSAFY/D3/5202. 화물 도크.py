def dfs(cnt):
    global visit, result, work

    if cnt < work:
        return

    if

    for i in range(N):
        if data[i][0] >= result[-1] and visit[i] == 0:
            visit[i] = 1
            result.append(data[i][0])
            result.append(data[i][1])
            cnt += 1
            dfs(cnt)
            visit[i] = 0
            result.pop()
            result.pop()


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    visit = [0]*N
    result = [0]
    work = 0