for t in range(1, int(input())+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    i = 0
    while i !=8:
        result.append(N//money[i])
        N = N%money[i]
        i +=1
    print('#{}'.format(t))
    print('{}'.format(' '.join(map(str, result))))