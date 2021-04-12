N = int(input())
stair = [int(input()) for i in range(N)]
dp = []
if N > 0:
    dp.append(stair[0])
if N > 1:
    dp.append(stair[0]+stair[1])
if N > 2:
    dp.append(max(stair[2]+stair[0], stair[2]+stair[1]))
for i in range(3, N):
    dp.append(max((stair[i]+stair[i-1]+dp[i-3]), (stair[i] + dp[i-2])))
print(dp[N-1])