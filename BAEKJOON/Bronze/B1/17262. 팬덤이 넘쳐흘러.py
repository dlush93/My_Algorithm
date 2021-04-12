N = int(input())
fan = [0, 100001]
time = [list(map(int, input().split())) for i in range(N)]
for t in time:
    if t[0] >= fan[0]:
        fan[0] = t[0]
    if t[1] <= fan[1]:
        fan[1] = t[1]
if fan[0] > fan[1]:
    print(fan[0] - fan[1])
else:
    print(0)