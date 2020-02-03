T = int(input())
for t in range(1, T+1):
    K,N,M = map(int,input().split())
    charge = list(map(int, input().split()))
    charge_lst = [0] * (N+1)
    for i in range(M):
        charge_lst[charge[i]] += 1
    start = 0
    end = K
    cnt = 0
    while True:
        zero = 0
        for i in range(start+1, end+1):
            if charge_lst[i] == 1:
                start = i
            else:
                zero += 1
        if zero == K:
            cnt = 0
            break
        cnt += 1
        end = start + K
        if end >= N:
            break
    print(f'#{t} {cnt}')