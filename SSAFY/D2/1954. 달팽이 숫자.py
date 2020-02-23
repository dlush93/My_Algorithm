dy, dx = [0,1,0,-1], [1,0,-1,0]
for t in range(1, int(input())+1):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    a = 1
    y = 0
    x = 0
    k = 0
    arr[y][x] = 1
    while a != N**2:
        if y+dy[k] < N and x+dx[k] < N and arr[y+dy[k]][x+dx[k]]==0:
            a+=1
            arr[y+dy[k]][x+dx[k]] = a
            y = y+dy[k]
            x = x+dx[k]
        else:
            if k ==3:
                k =0
            else:
                k+=1
    print('#{}'.format(t))
    for i in arr:
        print('{}'.format(' '.join(map(str, i))))