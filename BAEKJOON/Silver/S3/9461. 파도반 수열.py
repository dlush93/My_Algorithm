dp = [0]*101
dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7], dp[8], dp[9],dp[10] = 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
for t in range(int(input())):
    N = int(input())
    if N > 10:
        for i in range(11, N+1):
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])

