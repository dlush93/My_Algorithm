N, M = map(int, input().split())
switch = []
ramp_dict = dict()
for _ in range(N):
    ramp_on = list(map(int, input().split()))
    switch.append(ramp_on[1:])
    for on in ramp_on[1:]:
        if on not in ramp_dict:
            ramp_dict[on] = 0
        ramp_dict[on] += 1
result = 0
for ramp in switch:
    for off in ramp:
        if ramp_dict[off] == 1:
            result += 1
            break
if result == N:
    print(0)
else:
    print(1)