for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    a = M % N
    print('#{} {}'.format(t, data[a]))