# N = int(input())
# t = []
# p = []
# dp = [0]*(N+1)
# for i in range(N):
#     T, P = map(int, input().split())
#     t.append(T)
#     p.append(P)
#     dp[i] = P
# for i in range(N-1, -1, -1):
#     if i + t[i] > N:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], p[i]+dp[i + t[i]])
# print(dp[0])

def recursion(day, remain, money):
    if day == N:
        if remain > 0:
            return 0
        return money

    result = recursion(day+1, remain-1, money)
    if remain <= 0:
        result = max(result, recursion(day+1, counseling[day][0]-1, money+counseling[day][1]))
    return result


N = int(input())
counseling = [list(map(int, input().split())) for _ in range(N)]
print(recursion(0, 0, 0))