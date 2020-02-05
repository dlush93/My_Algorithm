test = int(input())
for t in range(1, test+1):
    data = input()
    a = len(data)
    arr = []
    card_dict = {'S':[1]*13, 'D':[1]*13, 'H':[1]*13, 'C':[1]*13}
    for i in range(int(a/3)):
        if data[i*3:i*3+3] not in arr:
            arr.append(data[i*3:i*3+3])
    for j in arr:
        card_dict[j[0]][int(j[1:3])-1] -=1
    if len(arr) != int(a/3):
        print('#{} ERROR'.format(t))
    else:
        print('#{} {} {} {} {}'.format(t, sum(card_dict['S']), sum(card_dict['D']), sum(card_dict['H']), sum(card_dict['C'])))