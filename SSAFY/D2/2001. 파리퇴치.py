T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for k in range(M):
                fly += sum(data[i+k][j:j+M])
            if result < fly:
                result = fly
    print('#{} {}'.format(t, result))
