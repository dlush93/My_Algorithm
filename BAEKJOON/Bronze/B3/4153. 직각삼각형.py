flag = True
while flag:
    length = sorted(list(map(int, input().split())))
    if sum(length) == 0:
        flag = False
    else:
        if length[2]**2 == length[1]**2 + length[0]**2:
            print('right')
        else:
            print('wrong')