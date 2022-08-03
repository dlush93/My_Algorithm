def ladder(cnt):
    if cnt > 3:
        return -1

    new_line = [l[:] for l in line]

    put_line(new_line, cnt)

    for i in range(N):
        if not chk_line(i, new_line):


def put_line(new_line, cnt):
    for _ in range(cnt):
        for i in range(M+1):
            for j in range(N-1):
                if new_line[i][j] == 0 and new_line[i][j+1] == 0:
                    new_line[i][j] = 1
                    new_line[i][j+1] = 1
                    for k in range(N):
                        if not chk_line(k, new_line):
                            break
                    else:
                        return cnt
                    new_line[i][j+1] = 0
                    new_line[i][j] = 0


def chk_line(num, now_line):
    col = 0
    row = num
    while col < M+1:
        if now_line[col][row] == 1:
            if num == 0:
                row += 1
            elif num == N-1:
                row -= 1
            else:
                if now_line[col][row+1] == 1:
                    row += 1
                else:
                    row -= 1
        col += 1
    if num == row:
        return True
    else:
        return False


N, M, H = map(int, input().split())
line = [[0 for _ in range(N)] for _ in range(M+1)]
for _ in range(M):
    a, b = map(int, input().split())
    line[a-1][b-1] = 1
    line[a-1][b] = 1
dx, dy = [1, 0, 0], [0, 1, -1]
print(line)
print(ladder(line, 0))