for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input())) for i in range(N)]
    result = 0
    for i in range(N//2+1):
        if i != N//2:
            result += sum(data[i][(N//2)-i:(N//2)+1+i])
            result += sum(data[N-i-1][(N//2)-i:(N//2)+1+i])
        else:
            result += sum(data[i][(N//2)-i:(N//2)+1+i])
    print('#{} {}'.format(t, result))