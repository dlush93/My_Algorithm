word1 = list(input())
word2 = list(input())
len1 = len(word1)
len2 = len(word2)
dp = [[0]*(len2+1) for i in range(len1+1)]
for i in range(1, len1+1):
    for j in range(1, len2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len1][len2])