N = int(input())
tip = []
for i in range(N):
    tip.append(int(input()))

money = 0
for idx, t in enumerate(sorted(tip, reverse=True), 1):
    if t - (idx - 1) > 0:
        money += t - (idx - 1)
print(money)