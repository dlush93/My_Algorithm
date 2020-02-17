for t in range(1, int(input())+1):
    N, R = map(int, input().split())
    a = 1
    for i in range(N, N-R, -1):
        a = (a*i/(N-i+1))%1234567891
    print('#{} {}'.format(t, a))