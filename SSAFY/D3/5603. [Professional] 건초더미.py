for t in range(1, int(input())+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(int(input()))
    avg = sum(data)//N
    result = 0
    for i in data:
        result += abs(i-avg)
    print('#{} {}'.format(t, result//2))