for t in range(1, int(input())+1):
    result = [1, 3]
    N = int(input())//10
    for i in range(1,N-1):
        result.append(result[i]+result[i-1]*2)
    print('#{} {}'.format(t, result[N-1]))