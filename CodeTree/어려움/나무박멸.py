dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
rx, ry = [-1, -1, 1, 1], [-1, 1, -1, 1]


def grow():
    for i in range(N):
        for j in range(N):
            cnt = 0
            if board[i][j] > 0:
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] > 0:
                            cnt += 1
                board[i][j] += cnt


def spread():
    new_board = [b[:] for b in board]
    for i in range(N):
        for j in range(N):
            temp = []
            if board[i][j] > 0:
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] == 0:
                            temp.append([nx, ny])
            for t in temp:
                new_board[t[0]][t[1]] += board[i][j]//len(temp)
    return new_board


def remove(time):
    max_remove = -1
    chk = [[-1 if i == -1 else 0 for i in b] for b in board]
    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0:
                continue
            remove_cnt = board[i][j]
            for k in range(4):
                for l in range(1, K+1):
                    nx, ny = i+rx[k]*l, j+ry[k]*l
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] <= 0:
                            break
                        else:
                            remove_cnt += board[nx][ny]
            chk[i][j] = remove_cnt

    for i in range(N):
        for j in range(N):
            if chk[i][j] > max_remove:
                max_remove = chk[i][j]
                remove_point = [i, j]

    board[remove_point[0]][remove_point[1]] = -1*(time+C)
    for k in range(4):
        for l in range(1, K+1):
            nx, ny = remove_point[0]+rx[k]*l, remove_point[1]+ry[k]*l
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == -1:
                    break
                elif board[nx][ny] < -1 or board[nx][ny] == 0:
                    board[nx][ny] = -1*(time+C)
                    break
                else:
                    board[nx][ny] = -1*(time+C)
    return max_remove


def end(time):
    if time == 1:
        return
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1*time:
                board[i][j] = 0


N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
for m in range(1, M+1):
    grow()
    board = spread()
    result += remove(m)
    end(m)
print(result)