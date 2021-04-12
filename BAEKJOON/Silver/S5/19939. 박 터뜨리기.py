N, K = map(int, input().split())
for i in range(1, K+1):
    N -= i
if N < 0:
    print(-1)
else:
    if N%K == 0:
        print(K-1)
    else:
        print(K)