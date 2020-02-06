for t in range(1, 11):
    tc = input()
    data = [list(map(int, input().split())) for i in range(100)]
    mini = 10000
    ans = 0
    for i in range(100):
        if data[0][i] == 1:
            x = i
            cnt = 0
        for j in range(1,100):
            if x != 0 and data[j][x-1] == 1:
                while x != 0 and data[j][x-1] == 1:
                    x -=1
                    cnt +=1
            elif x < 99 and data[j][x+1] == 1:
                while x < 99 and data[j][x+1] == 1:
                    x +=1
                    cnt +=1
            cnt +=1
        if mini >= cnt:
            mini = cnt
            ans = i
    print('#{} {}'.format(tc, ans))