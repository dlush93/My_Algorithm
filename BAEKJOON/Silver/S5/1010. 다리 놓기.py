for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    if N==M:
        print('1')
    else:
        a = 1
        b = max(M-N, N)
        for i in range(M,b,-1):
            a = int(a*i/(M-i+1))
        print(a)