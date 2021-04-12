n = int(input())
triangle = [list(map(int, input().split())) for i in range(n)]
dp = [[] for i in range(501)]
dp[0] = triangle[0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i].append(triangle[i][j] + dp[i-1][j])
        elif j == i:
            dp[i].append(triangle[i][j] + dp[i-1][j-1])
        else:
            dp[i].append(max(triangle[i][j]+ dp[i-1][j], triangle[i][j]+ dp[i-1][j-1]))
print(max(dp[n-1]))