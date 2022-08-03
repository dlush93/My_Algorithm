def now_board(board, cnt):
    global result
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if board[i][j] > result:
                    result = board[i][j]
        return

    for i in range(4):
        nb = [b[:] for b in board]
        nb = push(nb, i)
        nb = sum_block(nb, i)
        nb = push(nb, i)
        if board != nb:
            now_board(nb, cnt+1)


def sum_block(nb, direction):
    for i in range(N):
        if direction == 0:
            for j in range(N-1):
                if nb[j][i] == nb[j+1][i]:
                    nb[j][i] *= 2
                    nb[j+1][i] = 0
        elif direction == 1:
            for j in range(N-1):
                if nb[i][j] == nb[i][j+1]:
                    nb[i][j] *= 2
                    nb[i][j+1] = 0
        elif direction == 2:
            for j in range(N-1, 0, -1):
                if nb[j][i] == nb[j-1][i]:
                    nb[j][i] *= 2
                    nb[j-1][i] = 0
        else:
            for j in range(N-1, 0, -1):
                if nb[i][j] == nb[i][j-1]:
                    nb[i][j] *= 2
                    nb[i][j-1] = 0
    return nb


def push(nb, direction):
    for i in range(N):
        start, end = 0, 0
        if direction == 0:
            while end < N:
                if nb[end][i] != 0:
                    temp = nb[end][i]
                    nb[end][i] = 0
                    nb[start][i] = temp
                    start += 1
                end += 1
        elif direction == 1:
            while end < N:
                if nb[i][end] != 0:
                    temp = nb[i][end]
                    nb[i][end] = 0
                    nb[i][start] = temp
                    start += 1
                end += 1
        elif direction == 2:
            while end < N:
                if nb[N-1-end][i] != 0:
                    temp = nb[N-1-end][i]
                    nb[N-1-end][i] = 0
                    nb[N-1-start][i] = temp
                    start += 1
                end += 1
        else:
            while end < N:
                if nb[i][N-1-end] != 0:
                    temp = nb[i][N-1-end]
                    nb[i][N-1-end] = 0
                    nb[i][N-1-start] = temp
                    start += 1
                end += 1
    return nb


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
if N == 1:
    result = board[0][0]
else:
    now_board(board, 0)
print(result)