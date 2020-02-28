for t in range(1, int(input())+1):
    N = int(input())
    data1 = [list(map(int, input().split())) for i in range(N)]
    P = int(input())
    data2 = [int(input()) for i in range(P)]
    stack = []
    for i in data2:
        cnt = 0
        for j in data1:
            if j[0] <= i <= j[1]:
                cnt +=1
        stack.append(cnt)
    print('#{} {}'.format(t, ' '.join(map(str, stack))))