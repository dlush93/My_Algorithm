for t in range(1, int(input())+1):
    result = 0
    for i in range(1, int(input())+1):
        if i%2:
            result += i
        else:
            result -= i
    print('#{} {}'.format(t, result))