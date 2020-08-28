dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(start):
    stack = []
    stack.append(start)
    cnt = 1
    while stack:
        y,x = stack.pop()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if -1 < ny < N and -1 < nx < N:
                if data[y][x] + 1 == data[ny][nx]:
                    stack.append([ny,nx])
                    cnt +=1
    return cnt


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    max_num = 0
    room = 0
    for i in range(N):
        for j in range(N):
            if max_num < dfs([i, j]):
                room = data[i][j]
                max_num = dfs([i, j])
            elif max_num == dfs([i, j]):
                room = min(data[i][j], room)
    print('#{} {} {}'.format(t, room, max_num))