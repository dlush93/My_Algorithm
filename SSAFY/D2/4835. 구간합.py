test = int(input())
for t in range(1, test+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    result = []
    for i in range(N-M+1):
        a = sum(data[i:i+M])
        result.append(a)
    print('#{} {}'.format(t, max(result) - min(result)))