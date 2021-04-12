def tilt_chk(x, y, d):
    if d =='row':
        if abs(data[i][j-1] - data[i][j]) > 1:

N, L = map(int, input().split())
data = [list(map(int, input().split())) for i in range(N)]
arr = [[0]*N for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(1, N):
        if abs(data[i][j-1] - data[i][j]) > 1:
            break
        elif arr[i][j] == 1:
            continue
        else:

