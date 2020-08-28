dy ,dx = [1, 0], [0, 1]

def find(y,x, num):
    global result_min

    if num > result_min:
        return
    if y == N-1 and x == N-1:
        result_min = num
        return

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            num += data[ny][nx]
            find(ny, nx, num)
            visit[ny][nx] = 0
            num -= data[ny][nx]


for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    visit = [[0]*N for i in range(N) ]
    result_min = 2000
    find(0,0, data[0][0])
    print('#{} {}'.format(t, result_min))