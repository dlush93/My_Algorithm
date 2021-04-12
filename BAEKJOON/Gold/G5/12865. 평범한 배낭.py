N, K = map(int, input().split())
item = [[0, 0]] + [list(map(int, input().split())) for i in range(N)]
dp = [[0]*(K+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = item[i]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[N][K])