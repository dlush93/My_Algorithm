n = int(input())
num_list = list(map(int, input().split()))
dp = [0]*n
left = [0]*n
right = [0]*n
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] and left[i] < left[j]:
            left[i] = left[j]
    left[i] += 1
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if num_list[i] > num_list[j] and right[i] < right[j]:
            right[i] = right[j]
    right[i] += 1
for m in range(n):
    dp[m] = left[m] + right[m] - 1
print(max(dp))