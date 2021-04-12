for t in range(int(input())):
    N, M = input().split()
    cnt = 0
    chk1 = 0
    chk2 = 0
    chk3 = 0
    for i in range(len(N)):
        if N[i] == '1':
            chk1 += 1
        if M[i] == '1':
            chk2 += 1
        if N[i] != M[i]:
            chk3 += 1
    cnt += abs(chk1-chk2)
    cnt += (chk3 - cnt)//2
    print(cnt)
