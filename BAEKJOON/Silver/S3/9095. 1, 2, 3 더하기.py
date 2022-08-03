dp = [0 for _ in range(1000001)]
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 1000001):
    dp[i] = dp[i-1]%1000000009 + dp[i-2]%1000000009 + dp[i-3]%1000000009

for _ in range(int(input())):
    print(dp[int(input())]%1000000009)