def apples(start, cnt):
    pass


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
friends = [list(map(int, input().split())) for _ in range(M)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
result = 0
for f in friends:
    apples(f, 0)