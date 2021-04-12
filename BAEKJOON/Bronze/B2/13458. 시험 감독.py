n = int(input())
test = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0
for t in test:
    if t < b:
        cnt += 1
        continue
    else:
        t -= b
        cnt += 1
        if t%c != 0:
            cnt += t//c + 1
        else:
            cnt += t//c
print(cnt)
