n = int(input())
num_list = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
result = -1000
for i in range(1, n+1):
    dp[i] = max(dp[i-1]+num_list[i], num_list[i])
    result = max(dp[i], result)
print(result)