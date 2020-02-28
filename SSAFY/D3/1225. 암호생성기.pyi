def password(data):
    n = 1
    index = 0
    while data[index] !=0:
        if data[index] - n < 0:
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

for t in range(1, 2):
    input()
    data = list(map(int, input().split()))
    print(password(data))