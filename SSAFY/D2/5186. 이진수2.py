for t in range(1, int(input())+1):
    N = float(input())
    result = ''
    cnt = 0
    while N != 0.0:
        num = N*2
        if num >= 1:
            result += '1'
            cnt += 1
            N = num - 1
        else:
            result += '0'
            cnt += 1
            N = num
        if cnt > 13:
            result = 'overflow'
            break
    print('#{} {}'.format(t, result))