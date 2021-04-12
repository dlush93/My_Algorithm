for t in range(int(input())):
    J, N = map(int, input().split())
    box = []
    for i in range(N):
        R, C = map(int, input().split())
        box.append(R*C)
    cnt = 1
    for b in sorted(box, reverse=True):
        if J > b:
            J -= b
            cnt +=1
        else:
            break
    print(cnt)