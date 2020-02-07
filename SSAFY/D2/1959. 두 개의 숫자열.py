test = int(input())
for t in range(1, test+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MAX = max(N,M)
    MIN = min(N,M)
    MAX_SUM = 0
    if MAX - MIN == 0:
        for i in range(MAX):
            MAX_SUM += A[i]*B[i]
        print('#{} {}'.format(t, MAX_SUM))
        break
    elif N >  M:
        for i in range(MAX - MIN+1):
            SUM = 0
            for j in range(MAX):
                B1 = [0]*i + B + [0]*(MAX - MIN -i)
                SUM += A[j]*B1[j]
            if MAX_SUM < SUM :
                MAX_SUM = SUM
    else:
        for i in range(MAX - MIN+1):
            SUM = 0
            for j in range(MAX):
                A1 = [0]*i + A + [0]*(MAX - MIN -i)
                SUM += A1[j]*B[j]
            if MAX_SUM < SUM :
                MAX_SUM = SUM
    print('#{} {}'.format(t, MAX_SUM))