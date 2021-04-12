N, S, R = map(int, input().split())
damaged = list(map(int, input().split()))
extra = list(map(int, input().split()))
kayak = [1]*N
for d in damaged:
    kayak[d-1] -= 1
for e in extra:
    kayak[e-1] += 1
for idx, k in enumerate(kayak):
    if idx == 0:
        if k == 2 and kayak[idx+1] == 0:
            kayak[idx] = 1
            kayak[idx+1] = 1
    elif 0 < idx < N-1:
        if k == 2 and kayak[idx-1] == 0:
            kayak[idx] = 1
            kayak[idx - 1] = 1
        elif k == 2 and kayak[idx+1] == 0:
            kayak[idx] = 1
            kayak[idx+1] = 1
    elif idx == N-1:
        if k == 2 and kayak[idx-1] == 0:
            kayak[idx] = 1
            kayak[idx-1] = 1
cnt = 0
for k in kayak:
    if k == 0:
        cnt +=1
print(cnt)