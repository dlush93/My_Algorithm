def move(order):
    if order == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif order == 2:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif order == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]


def chk(nx, ny):
    if arr[nx][ny] != 0:
        dice[0] = arr[nx][ny]
        arr[nx][ny] = 0
    else:
        arr[nx][ny] = dice[0]
    print(dice[5])


N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
orders = list(map(int, input().split()))
dice = [0]*6
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
for order in orders:
    if 0 <= x + dx[order-1] < N and 0 <= y + dy[order-1] < M:
        x += dx[order-1]
        y += dy[order - 1]
        move(order)
        chk(x, y)