N, P, K, W = map(int, input().split())
power = 0
cnt=0
while power < K:
    power += W
    cnt += 1
print(cnt)