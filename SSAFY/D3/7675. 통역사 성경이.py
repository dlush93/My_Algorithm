end = ['.', '!', '?']

for t in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    data = []
    temp = []
    while cnt != N:
        word = list(input().split())
        for i in word:
            for j in i:
                if j in end:
                    temp.append(i)
                    data.append(temp)
                    cnt +=1
                    temp = []
                    break
            else:
                temp.append(i)
    name = []
    for i in range(N):
        name_cnt = 0
        for j in data[i]:
            if j == data[i][-1]:
                if j[0:-1].isalpha():
                    if len(j[0:-1]) == 1 and j[0].isupper():
                        name_cnt +=1
                    else:
                        if j[0].isupper() and j[1:-1].islower():
                            name_cnt +=1
            elif j.isalpha() and j[0].isupper() and j[1:-1].islower():
                name_cnt +=1
        name.append(name_cnt)
    print('#{} {}'.format(t, ' '.join(map(str, name))))

