from collections import deque


def rotate(x, d, k):
    for i in range(x-1, N, x):
        if d == 0:
            plate[i].rotate(k)
        else:
            plate[i].rotate(k*-1)


def change():
    delete = set()
    for i in range(N):
        for j in range(M):
            if plate[i][j] != 0:
                if j == M-1:
                    if plate[i][j] == plate[i][0]:
                        delete.add((i, j))
                        delete.add((i, 0))
                else:
                    if plate[i][j] == plate[i][j+1]:
                        delete.add((i, j))
                        delete.add((i, j+1))
                if i != N-1:
                    if plate[i][j] == plate[i+1][j]:
                        delete.add((i, j))
                        delete.add((i+1, j))

    num = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if (i, j) in delete:
                plate[i][j] = 0
            else:
                num += plate[i][j]
                if plate[i][j] != 0:
                    cnt += 1
    if cnt == 0:
        avg = 0
    else:
        avg = num/cnt
    if len(delete) == 0:
        for i in range(N):
            for j in range(M):
                if plate[i][j] != 0:
                    if plate[i][j] > avg:
                        plate[i][j] -= 1
                    elif plate[i][j] < avg:
                        plate[i][j] += 1


N, M, T = map(int, input().split())
plate = [deque(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    rotate(*map(int, input().split()))
    change()
result = 0
for i in range(N):
    for j in range(M):
        result += plate[i][j]
print(result)