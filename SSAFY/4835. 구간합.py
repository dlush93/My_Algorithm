import sys
test = int(input())
for t in range(1,test+1):
    N, M = map(int, input().split())
    data = list(map(sys.stdin.readline().split()))
    max_sum = 0
    min_sun = 0
    for i in range(N-M+1):
        for m in range(M):
            a += data[i+m]
        if i == 0:
            max_sum = a
            min_sum = a
        if a >