N = int(input())
name = [input().split('.') for i in range(N)]
exe = sorted([name[i][1] for i in range(N)])
now_exe = exe[0]
cnt = 0
for i in exe:
    if i == now_exe:
        cnt += 1
    else:
        print(now_exe, cnt)
        now_exe = i
        cnt = 1
else:
    print(now_exe, cnt)