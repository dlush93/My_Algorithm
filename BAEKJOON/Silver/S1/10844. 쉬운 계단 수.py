N = int(input())
dp = [[0] * 10 for i in range(N+1)]
dp[1] = [1]*10
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
print(sum(dp[N][1:])%1000000000)