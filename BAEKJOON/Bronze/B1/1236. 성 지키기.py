N, M = map(int, input().split())
castle = [input() for i in range(N)]
row = [1 for _ in range(N)]
col = [1 for _ in range(M)]
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 0
            col[j] = 0
print(max(sum(row), sum(col)))