test = int(input())
for t in range(1,test+1):
    N = int(input())
    arr = [[1]+[0]*(N-1) for i in range(N)]
    for i in range(N):
        arr[i][i] = 1
    for j in range(2,N):
        for k in range(1,N-1):
            arr[j][k] = arr[j-1][k]+arr[j-1][k-1]
    a = 0
    print('#{}'.format(t))
    for q in arr:
        print(' '.join(map(str, q[0:a+1])))
        a+=1