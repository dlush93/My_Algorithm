def set_cctv(cnt, now_office):
    if cnt == len(cctv):
        none_sight_chk(now_office)
        return



    if cctv[cnt][2] == 1 or cctv[cnt][2] == 3 or cctv[cnt][2] == 4:
        for i in range(4):
            new_office = [o[:] for o in now_office]
            new_office = sight(cctv[cnt], i, new_office)
            set_cctv(cnt+1, new_office)
    elif cctv[cnt][2] == 2:
        for i in range(2):
            new_office = [o[:] for o in now_office]
            new_office = sight(cctv[cnt], i, new_office)
            set_cctv(cnt + 1, new_office)
    else:
        new_office = [o[:] for o in now_office]
        new_office = sight(cctv[cnt], 0, new_office)
        set_cctv(cnt + 1, new_office)


def sight(cctv_num, direc, new_office):
    stack = []
    if cctv_num[2] == 1:
        stack.append([cctv_num[0], cctv_num[1]])
        while stack:
            x, y = stack.pop()
            nx, ny = x+dx[direc], y+dy[direc]
            if 0 <= nx < N and 0 <= ny < M:
                if new_office[nx][ny] != 6:
                    new_office[nx][ny] = '#'
                    stack.append([nx, ny])

    elif cctv_num[2] == 2:
        for i in range(0, 4, 2):
            stack.append([cctv_num[0], cctv_num[1]])
            while stack:
                x, y = stack.pop()
                nx, ny = x+dx[direc+i], y+dy[direc+i]
                if 0 <= nx < N and 0 <= ny < M:
                    if new_office[nx][ny] != 6:
                        new_office[nx][ny] = '#'
                        stack.append([nx, ny])

    elif cctv_num[2] == 3:
        for i in range(2):
            stack.append([cctv_num[0], cctv_num[1]])
            while stack:
                x, y = stack.pop()
                nx, ny = x + dx[(direc + i)%4], y + dy[(direc + i)%4]
                if 0 <= nx < N and 0 <= ny < M:
                    if new_office[nx][ny] != 6:
                        new_office[nx][ny] = '#'
                        stack.append([nx, ny])

    elif cctv_num[2] == 4:
        for i in range(3):
            stack.append([cctv_num[0], cctv_num[1]])
            while stack:
                x, y = stack.pop()
                nx, ny = x + dx[(direc + i)%4], y + dy[(direc + i)%4]
                if 0 <= nx < N and 0 <= ny < M:
                    if new_office[nx][ny] != 6:
                        new_office[nx][ny] = '#'
                        stack.append([nx, ny])
    else:
        for i in range(4):
            stack.append([cctv_num[0], cctv_num[1]])
            while stack:
                x, y = stack.pop()
                nx, ny = x + dx[direc + i], y + dy[direc + i]
                if 0 <= nx < N and 0 <= ny < M:
                    if new_office[nx][ny] != 6:
                        new_office[nx][ny] = '#'
                        stack.append([nx, ny])

    return new_office


def none_sight_chk(now_office):
    global result
    cnt = 0
    for row in now_office:
        cnt += row.count(0)
    result = min(result, cnt)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = [(i, j, office[i][j]) for i in range(N) for j in range(M) if 0 < office[i][j] < 6]
result = N*M
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
set_cctv(0, office)
print(result)