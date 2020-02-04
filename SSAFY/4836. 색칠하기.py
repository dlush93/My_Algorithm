test = int(input())
for t in range(1,test+1):
    color = [[0] * 10 for i in range(10)]
    N = int(input())
    count=0
    for n in range(N):
        a = list(map(int,input().split()))
        for i in range(a[0], a[2]+1):
            for j in range(a[1], a[3]+1):
                color[i][j] += a[4]
                if color[i][j] ==3:
                    count+=1
    print('#{} {}'.format(t, count))