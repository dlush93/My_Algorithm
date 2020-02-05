test = int(input())
for t in range(1,test+1):
    N = int(input())
    v = 0
    s = 0
    for i in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] ==0:
            v = v
            s += v*1
        elif cmd[0] ==1:
            v += cmd[-1]
            s += v*1
        else:
            if v > cmd[-1]:
                v -= cmd[-1]
                s += v*1
            else:
                v = 0
                s += v*1
    print('#{} {}'.format(t, s))