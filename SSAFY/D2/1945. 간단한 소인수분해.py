for t in range(1, int(input())+1):
    N = int(input())
    a = [2,3,5,7,11]
    i = 0
    j = 0
    result = []
    while i != 5:
        if N%a[i] ==0:
            j +=1
            N = N//a[i]
        else:
            result.append(j)
            j = 0
            i +=1
    print('#{} {}'.format(t, ' '.join(map(str, result))))