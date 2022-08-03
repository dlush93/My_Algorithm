import sys
sys.setrecursionlimit(10000)


def move(cnt):
    if cnt > 1000:
        return -1

    for s in sorted(shark):
        x, y = shark[s]
        direc = direction[s-1]
        move_direc = prefer[(s-1)*4+direc-1]
        for d in move_direc:
            nx, ny = x+dx[d-1], y+dy[d-1]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny][0] == 0:
                    if board[nx][ny][1] == 0 or board[nx][ny][1] < cnt:
                        board[x][y][0] = 0
                        board[nx][ny] = [s, K+cnt, s]
                        shark[s] = [nx, ny]
                        direction[s-1] = d
                        break
                elif board[nx][ny][1] < cnt and board[nx][ny] != s:
                    del shark[s]
                    board[x][y][0] = 0
                    break
        else:
            for d in move_direc:
                nx, ny = x+dx[d-1], y+dy[d-1]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny][2] == s:
                        board[x][y][0] = 0
                        board[nx][ny] = [s, K+cnt, s]
                        shark[s] = [nx, ny]
                        direction[s-1] = d
                        break
    print('------------', cnt)
    print(shark)
    for b in board:
        print(b)
    if len(shark) == 1:
        return cnt
    else:
        return move(cnt+1)


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 0:
            board[i][j] = [0, 0, 0]
        else:
            board[i][j] = [arr[j], K, arr[j]]
direction = list(map(int, input().split()))
prefer = [list(map(int, input().split())) for _ in range(M*4)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
shark = dict()
for i in range(N):
    for j in range(N):
        if board[i][j][0] != 0:
            shark[board[i][j][0]] = [i, j]
print(move(1))