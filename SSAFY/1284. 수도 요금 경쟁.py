test = int(input())
for t in range(1,test+1):
    P, Q, R, S, W = map(int, input().split())
    if R > W:
        if P*W < Q:
            print('#{} {}'.format(t, P*W))
        else:
            print('#{} {}'.format(t, Q))
    else:
        if P*W < Q + (W-R)*S:
            print('#{} {}'.format(t, P * W))
        else:
            print('#{} {}'.format(t, Q + (W-R)*S))