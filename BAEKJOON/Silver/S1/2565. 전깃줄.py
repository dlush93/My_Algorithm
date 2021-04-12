n = int(input())
line = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x:x[0])
dp = [0]*n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n-max(dp))