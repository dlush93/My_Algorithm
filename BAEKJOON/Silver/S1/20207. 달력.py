def schedule_chk(s, e):
    for i in range(s, e+1):
        days[i] += 1


N = int(input())
days = [0 for _ in range(366)]
schedules = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
start, end = schedules[0]
schedule_chk(start, end)
size = 0
for i in range(1, N):
    if schedules[i][0] <= end+1:
        end = max(schedules[i][1], end)
        schedule_chk(schedules[i][0], schedules[i][1])
    else:
        size += (end-start+1)*max(days[start:end+1])
        start = schedules[i][0]
        end = schedules[i][1]
        schedule_chk(start, end)
else:
    size += (end-start+1) * max(days[start:end+1])
print(size)