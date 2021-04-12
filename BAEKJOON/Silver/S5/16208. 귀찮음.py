n = int(input())
stick = sorted(list(map(int, input().split())))
cost = 0
long_stick = sum(stick)
for s in range(len(stick)):
    long_stick -= s
    cost += (long_stick)*s
print(cost)