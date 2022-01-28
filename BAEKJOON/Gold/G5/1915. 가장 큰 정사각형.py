dx, dy = [-1, -1, 0], [0, -1, -1]

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        min_area = n*m+1
        if arr[i][j] == '1':
            for k in range(3):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < n and 0 <= y < m:
                    min_area = min(dp[x][y], min_area)
            else:
                if min_area == n*m+1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min_area + 1
                    result = max(result, dp[i][j])
        else:
            dp[i][j] = 0
print(result**2)