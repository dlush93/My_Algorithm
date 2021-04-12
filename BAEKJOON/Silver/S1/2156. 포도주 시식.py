n = int(input())
wine = [0] + [int(input()) for i in range(n)]
dp = [0]*(n+1)
for i in range(1, n+1):
    if i == 1:
        dp[1] = wine[1]
    elif i == 2:
        dp[2] = wine[2] + wine[1]
    else:
        dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2], dp[i-1])
print(dp[n])


# def dfs(x):
#     if dp[x] is not None:
#         return dp[x]
#
#     dp[x] = max(wine[x] + wine[x-1] + dfs(x-3), wine[x] + dfs(x-2), dfs(x-1))
#     return dp[x]
#
#
# dp = [0] + [None] * 10000
# dp[1] = wine[1]
# dp[2] = wine[2] + wine[1]
# print(dfs(n))
