for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = [list(input()) for i in range(N)]
    cnt = 0
    for d in data[0]:
        if d != 'W':
            cnt += 1
    for d in data[N-1]:
        if d != 'R':
            cnt += 1
