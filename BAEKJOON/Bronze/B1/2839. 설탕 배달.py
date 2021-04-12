N = int(input())
cnt = 0
sugar = 0
while cnt != 5:
    if N%5 == 0:
        sugar = N//5 + cnt
        break
    elif cnt !=5 and N - 3 < 0:
        cnt = 5
    else:
        N -= 3
        cnt += 1
if cnt == 5:
    print(-1)
else:
    print(sugar)