for t in range(1, int(input())+1):
    N, R = map(int, input().split())
    a = 1
    c = max(R-N, N)
    for i in range(R, c, -1):
        a = a*i/(N-i+1)
    print('{}'.format(int(a)))