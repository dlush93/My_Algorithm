def password(data):
    n = 1
    index = 0
    while data[index] !=0:
        if data[index] - n <= 0:
            data[index] = 0
            break
        else:
            data[index] -= n
            if n ==5:
                n = 1
            else:
                n+=1
            if index ==7:
                index = 0
            else:
                index +=1
    return data

for t in range(1, 11):
    input()
    data = list(map(int, input().split()))
    password(data)
    for i in range(8):
        if data[i] == 0:
            for j in range(7-i):
                a = data.pop()
                data.insert(0,a)
    print('#{} {}'.format(t, ' '.join(map(str, data))))