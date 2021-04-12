N, K = map(int, input().split())
value = sorted([int(input()) for i in range(N)], reverse=True)
cnt = 0
for i in range(N):
    if value[i] > K:
        continue
    else:
        cnt += K//value[i]
        K = K%value[i]
print(cnt)