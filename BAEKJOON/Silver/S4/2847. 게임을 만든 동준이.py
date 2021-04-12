N = int(input())
point = [int(input()) for i in range(N)]
cnt = 0
for i in range(N-2, -1, -1):
    if point[i+1] <= point[i]:
        cnt += point[i] - point[i+1] + 1
        point[i] -= point[i] - point[i+1] + 1
print(cnt)