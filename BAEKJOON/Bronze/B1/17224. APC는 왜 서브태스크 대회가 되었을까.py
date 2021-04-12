N, L, K = map(int, input().split())
test = [list(map(int, input().split())) for i in range(N)]
problem = [0] * N
cnt = 0
point = 0
for i in range(N):
    if test[i][1] <= L and cnt != K:
        problem[i] = 1
        cnt += 1
        point += 140
for idx, p in enumerate(problem):
    if p == 0 and cnt != K:
        if test[idx][0] <= L:
            cnt += 1
            point += 100
    if cnt == K:
        break
print(point)