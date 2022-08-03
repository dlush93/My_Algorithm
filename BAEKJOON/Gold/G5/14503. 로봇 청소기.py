def clean(start, direc):
    cnt = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    flag_cnt = 0
    x, y = start
    visited[x][y] = 1
    while True:
        direc = (direc - 1) % 4
        if clean_chk(x, y, direc, visited):
            x, y = x+dx[direc], y+dy[direc]
            visited[x][y] = 1
            cnt += 1
            flag_cnt = 0
        else:
            flag_cnt += 1
        if flag_cnt == 4:
            if board[x+dx[(direc-2)%4]][y+dy[(direc-2)%4]] == 1:
                return cnt
            else:
                x, y = x+dx[(direc-2)%4], y+dy[(direc-2)%4]
                flag_cnt = 0


def clean_chk(x, y, direc, visited):
    nx, ny = x+dx[direc], y+dy[direc]
    if board[nx][ny] == 0:
        if visited[nx][ny] == 0:
            return True
    return False


N, M = map(int, input().split())
r, c, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
print(clean((r, c), direction))