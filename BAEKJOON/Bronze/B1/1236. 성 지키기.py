N, M = map(int, input().split())
castle = [list(input()) for i in range(N)]
security = []
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            security.append([i,j])
if N <= M :
    security_list = [1]*(N+1)
    for i in security:
        security_list[i[0]] = 0
    print(sum(security_list)-1)

else:
    security_list = [1]*(M+1)
    for i in security:
        security_list[i[1]] = 0
    print(sum(security_list)-1)