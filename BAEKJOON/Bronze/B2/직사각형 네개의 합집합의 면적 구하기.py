arr = [[0]*101 for i in range(101)]
cnt = 0
for t in range(4):
    a = list(map(int, input().split()))
    for i in range(a[0],a[2]):
        for j in range(a[1],a[3]):
            if arr[i][j] == 0:
                arr[i][j] += 1
                cnt += 1
print(cnt)