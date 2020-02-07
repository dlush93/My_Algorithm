test = int(input())
for t in range(1,test+1):
    data = [list(map(int, input().split())) for i in range(9)]
    a = list(range(1,10))
    b = True
    for i in range(9):
        result1 = []
        result2 = []
        for j in range(9):
            result1.append(data[i][j])
            result2.append(data[j][i])
        result1.sort()
        result2.sort()
        if result1 != a or result2 != a:
            print('#{} 0'.format(t))
            b = False
            break
    if b==True:
        for i in range(3):
            for j in range(3):
                result = []
                for k in range(3):
                    for l in range(3):
                        result.append(data[k+3*j][l+3*i])
                result.sort()
                if result != a:
                    print('#{} 0'.format(t))
                    b = False
                    break
            if b == False:
                break
    if b==True:
        print('#{} 1'.format(t))