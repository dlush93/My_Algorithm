A = list(range(1,13))
test = int(input())
for t in range(1, test+1):
    N, K = map(int, input().split())
    n = len(A)
    count = 0
    for i in range(1<<n):
        result = []
        for j in range(n):
            if i & (1<<j):
                result.append(A[j])
        if len(result) == N and sum(result) == K:
            count +=1
    print('#{} {}'.format(t, count))