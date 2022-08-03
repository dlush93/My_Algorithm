M, S = map(int, input().split()) # 물고기 수, 상어가 마법 연습한 횟수
MAP = [[[] for _ in range(4)] for _ in range(4)] # 4x4 격자
for _ in range(M):
    a, b, direction = map(int, input().split())
    MAP[a-1][b-1].append(direction)
shark = list(map(int, input().split()))
MAP[shark[0]-1][shark[1]-1].append('s')
fx, fy = [1, 0, -1, -1, -1, 0, 1, 1], [-1, -1, -1, 0, 1, 1, 1, 0]
sx, sy = [-1, 0, 1, 0], [0, -1, 0, 1]