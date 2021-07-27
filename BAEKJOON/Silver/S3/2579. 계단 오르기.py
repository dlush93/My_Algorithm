# 바텀업
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

# 탑다운
# import sys
# sys.setrecursionlimit(20000)
# input = sys.stdin.readline
#
#
# def top_down(n):
#     if n == 1:
#         dp[1] = stair[1]
#         return dp[1]
#     if n == 2:
#         dp[2] = stair[2] + stair[1]
#         return dp[2]
#     if n == 3:
#         dp[3] = max(stair[3]+stair[1], stair[3] + stair[2])
#         return dp[3]
#     if n > 3 and dp[n] == 0:
#         dp[n] = max(stair[n]+stair[n-1]+top_down(n-3),
#                     stair[n] + top_down(n-2))
#         return dp[n]
#     return dp[n]
#
#
# N = int(input())
# stair = [0] + [int(input()) for _ in range(N)]
# dp = [0 for _ in range(N+1)]
# print(top_down(N))