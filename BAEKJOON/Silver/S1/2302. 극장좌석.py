N = int(input())
M = int(input())
vip = set(int(input()) for _ in range(M))
seat = [1, 1, 2]
for i in range(3, 41):
    seat.append(seat[i-1] + seat[i-2])

if M:
    cnt = 0
    ans = 1
    for i in range(1, N+1):
        if i in vip:
            ans *= seat[cnt]
            cnt = 0
        else:
            cnt += 1
    else:
        ans *= seat[cnt]
    print(ans)
else:
    print(seat[N])