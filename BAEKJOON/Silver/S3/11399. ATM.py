N = int(input())
time = sorted(list(map(int, input().split())))
sum_time = 0
wait_time = 0
for t in time:
    wait_time += t
    sum_time += wait_time
print(sum_time)