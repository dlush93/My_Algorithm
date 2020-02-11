for t in range(1, int(input())+1):
    str1, str2 = input(), input()
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt+=1
        result = max(result,cnt)
    print('#{} {}'.format(t, result))