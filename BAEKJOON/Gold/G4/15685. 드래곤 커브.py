def dragon_curve(dragon):
    x, y, d, g = dragon
    stack = []
    arr[y][x] = 1
    stack.append(d)
    nx, ny = x+dx[d], y+dy[d]
    arr[ny][nx] = 1
    for _ in range(g):
        for i in range(len(stack)-1, -1, -1):
            nd = (stack[i]+1)%4
            nx, ny = nx+dx[nd], ny+dy[nd]
            arr[ny][nx] = 1
            stack.append(nd)


def point_chk():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                if arr[i+1][j] == 1 and arr[i+1][j+1] == 1 and arr[i][j+1] == 1:
                    cnt += 1
    return cnt


N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for _ in range(N):
    dragon = list(map(int, input().split()))
    dragon_curve(dragon)
print(point_chk())