dx, dy = [[-1, 0, 1, 0], [1, 0, -1, 0]], [[0, 1, 0, -1], [0, 1, 0, -1]]
import sys
input = sys.stdin.readline


def diffusion_dust(t):
    new_arr = [[0 for _ in range(C)] for _ in range(R)]
    new_chk = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if arr[r][c] == -1:
                new_arr[r][c] = -1
            if dust_chk[r][c] == t:
                cnt = 0
                new_chk[r][c] = t + 1
                for i in range(4):
                    nx, ny = r + dx[0][i], c + dy[0][i]
                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                        cnt += 1
                        new_arr[nx][ny] += int(arr[r][c]/5)
                        new_chk[nx][ny] = t + 1
                new_arr[r][c] += arr[r][c] - cnt*int(arr[r][c]/5)

    return new_arr, new_chk


def air_clean(cleaner):
    cx = cleaner[0]
    stack = [cleaner]
    cnt = 0
    while stack:
        x, y, p = stack.pop()
        nx, ny = x + dx[p][cnt], y + dy[p][cnt]
        if p == 0:
            if 0 <= nx < cx+1 and 0 <= ny < C:
                if arr[x][y] == -1:
                    stack.append((nx, ny, p))
                elif arr[nx][ny] == -1:
                    dust_chk[x][y] = 0
                    arr[x][y] = 0
                else:
                    arr[x][y] = arr[nx][ny]
                    dust_chk[x][y] = dust_chk[nx][ny]
                    stack.append((nx, ny, p))
            else:
                cnt += 1
                stack.append((x, y, p))
        else:
            if cx <= nx < R and 0 <= ny < C:
                if arr[x][y] == -1:
                    stack.append((nx, ny, p))
                elif arr[nx][ny] == -1:
                    dust_chk[x][y] = 0
                    arr[x][y] = 0
                else:
                    arr[x][y] = arr[nx][ny]
                    dust_chk[x][y] = dust_chk[nx][ny]
                    stack.append((nx, ny, p))
            else:
                cnt += 1
                stack.append((x, y, p))


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(R)]
cleaner = []
dust_chk = [[-1 for _ in range(C)] for i in range(R)]
result = 2
for r in range(R):
    for c in range(C):
        if arr[r][c] == -1:
            cleaner.append((r, c, len(cleaner)))
        elif arr[r][c] > 0:
            dust_chk[r][c] = 0

for t in range(T):
    arr, dust_chk = diffusion_dust(t)
    for cl in cleaner:
        air_clean(cl)

for a in arr:
    result += sum(a)

print(result)