def kick(s, t, cnt):
    global min_kick
    if s > t:
        return
    elif s == t:
        min_kick = min(min_kick, cnt)
        return
    else:
        kick(s*2, t+3, cnt+1)
        kick(s+1, t, cnt+1)

for t in range(int(input())):
    S, T = map(int, input().split())
    min_kick = T - S
    kick(S, T, 0)
    print(min_kick)