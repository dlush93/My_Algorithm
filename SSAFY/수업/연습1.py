while len(data) != 1:
    a_group = []
    b_group = []
    while len(a_group) != 1:
        cnt = 0
        a_data = data[0: (data[0][0] + data[-1][0]) // 2]
        for i in range(len(a_data)):
            print(a_group)
            a_group.append(data[i])
            cnt += 1
            if cnt % 2 == 0:
                b = a_group.pop()
                a = a_group.pop()
                a_group.append(rps(a, b))
        a_data = a_group
    while len(b_group) != 1:
        cnt = 0
        b_data = data[(data[0][0] + data[-1][0]) // 2: data[-1][0]]
        for i in range(len(b_data)):
            b_group.append(data[i])
            cnt += 1
            if cnt % 2 == 0:
                b = b_group.pop()
                a = b_group.pop()
                b_group.append(rps(a, b))
        b_data = b_group
    if rps(a_group[0], b_group[0]) == a_group:
        data = data[0: (data[0][0] + data[-1][0]) // 2]
    else:
        data = data[(data[0][0] + data[-1][0]) // 2: data[-1][0]]
print('#{} {}'.format(t, data[0][0]))