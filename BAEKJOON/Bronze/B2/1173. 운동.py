N, m, M, T, R = map(int, input().split())
# N 운동시간, m 최저맥박, M 최대맥박, T 맥박증가, R 맥박감소
time = 0
cnt = 0
now = m
while cnt < N:
    if time == 0 and m+T > M:
        print(-1)
        break
    if now+T <= M:
        now += T
        time += 1
        cnt += 1
    else:
        if now - R < m:
            now = m
            time +=1
        else:
            now -= R
            time +=1
else:
    print(time)