dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(i, j, cnt):
    stack = []
    visit = [[0]*N for i in range(N)]
    stack.append([i,j,cnt])

    while stack :
        y, x, cnt = stack.pop(0)
        if visit[y][x] == 0:
            visit[y][x] = 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if data[ny][nx] == '0':
                        stack.append([ny, nx, cnt + 1])
                    elif data[ny][nx] == '3':
                        return cnt
    return 0


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(input()) for i in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == '2':
                print('#{} {}'.format(t, bfs(i, j, 0)))
                break