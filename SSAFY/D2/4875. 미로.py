dy, dx = [-1,1,0,0], [0,0,-1,1]

def start(data, N):
    for i in range(N):
        for j in range(N):
            if data[i][j] =='2':
                return [i,j]

def dfs(start_node, N):

    stack = []
    visit = [[0]*N for i in range(N)]
    stack.append(start_node)
    while stack:
        y, x = stack.pop()
        if visit[y][x] == 0:
            visit[y][x] =1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if data[ny][nx] =='0':
                        stack.append([ny,nx])
                    elif data[ny][nx] =='3':
                        return 1
    return 0


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(input()) for i in range(N)]
    print('#{} {}'.format(t, dfs(start(data, N), N)))