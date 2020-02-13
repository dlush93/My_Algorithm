for t in range(1,11):
    input()
    data = [input().split() for i in range(100)]
    i = 99
    for j in range(100):
        if data[i][j] == '2':
            a = j
            break
    while i != 0:
        i -=1
        if a != 0 and data[i][a-1] =='1':
            while a !=0 and data[i][a-1] =='1':
                a -=1
        elif a < 99 and data[i][a+1] =='1':
            while a < 99 and data[i][a+1] =='1':
                a +=1
    print('#{} {}'.format(t, a))