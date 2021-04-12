dy, dx = [-1, 0, 1, 0 ], [0, 1, 0, -1]
def check(where):
    global result
    y, x = where
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            if data[ny][nx] == 'W':
                result = 0
                return
            elif data[ny][nx] =='.':
                data[ny][nx] = 'D'


R, C = map(int, input().split())
data = [list(input()) for i in range(R)]
sheep = []
result = 1
for i in range(R):
    for j in range(C):
        if data[i][j] == 'S':
            check([i,j])
if result == 0:
    print(result)
else:
    print(result)
    for i in data:
        print(''.join(i))