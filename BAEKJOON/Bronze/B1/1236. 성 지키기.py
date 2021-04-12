N, M = map(int, input().split())
castle = [list(input()) for i in range(N)]
security_row = [1]*M
security_colomn = [1]*N
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            security_row[j] = 0
            security_colomn[i] = 0
if sum(security_row) >= sum(security_colomn):
    print(sum(security_colomn))
else:
    print(sum(security_row))
