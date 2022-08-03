from collections import deque


def grow():
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                die = 0
                for _ in range(len(field[i][j])):
                    tree = field[i][j].popleft()
                    if tree <= soil[i][j]:
                        soil[i][j] -= tree
                        field[i][j].append(tree+1)
                    else:
                        die += tree//2
                soil[i][j] += die


def breed():
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                for k in range(len(field[i][j])):
                    if field[i][j][k]%5 == 0:
                        for l in range(8):
                            if 0 <= i+dx[l] < N and 0 <= j+dy[l] < N:
                                field[i+dx[l]][j+dy[l]].appendleft(1)


def spray_drug():
    for i in range(N):
        for j in range(N):
            soil[i][j] += drug[i][j]


N, M, K = map(int, input().split())
field = [[deque() for _ in range(N)] for _ in range(N)]
soil = [[5 for _ in range(N)] for _ in range(N)]
drug = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    field[x-1][y-1].append(z)
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    grow()
    breed()
    spray_drug()
result = 0
for i in range(N):
    for j in range(N):
        if field[i][j]:
            result += len(field[i][j])
print(result)