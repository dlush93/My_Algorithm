# def w(a, b, c, dp):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20, dp)
#     if dp[a][b][c] != 0:
#         return dp[a][b][c]
#
#     if a < b and b < c:
#         dp[a][b][c] = w(a, b, c-1, dp) + w(a, b-1, c-1, dp) - w(a, b-1, c, dp)
#     else:
#         dp[a][b][c] = w(a-1, b, c, dp) + w(a-1, b-1, c, dp) + w(a-1, b, c-1, dp) - w(a-1, b-1, c-1, dp)
#
#     return dp[a][b][c]
#
#
# dp = [[[0]*21 for i in range(21)] for j in range(21)]
#
# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == -1:
#         break
#     print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c, dp)))


def w(a, b, c):
    global dp
    if (a, b, c) in dp.keys():
        return dp[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        dp[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[(a, b, c)]


dp = dict()
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))