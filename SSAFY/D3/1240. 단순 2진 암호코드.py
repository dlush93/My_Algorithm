code = {
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9',
}

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = ''
    result = ''
    cnt = 0
    for i in range(N):
        data = input()
        if '1' in data:
            arr=data
    n = 0
    while len(result) != 8:
        if arr[n+cnt*7:n+cnt*7+7] in code:
            result += code[arr[n + cnt * 7:n + cnt * 7 + 7]]
            cnt += 1
        else:
            cnt = 0
            n += 1
            result = ''
    password = (int(result[0])+int(result[2])+int(result[4])+int(result[6]))*3 + int(result[1])+int(result[3])+int(result[5])+int(result[7])
    if password%10 == 0:
        print('#{} {}'.format(t, int(result[0])+int(result[1])+int(result[2])+int(result[3])+int(result[4])+int(result[5])+int(result[6])+int(result[7])))
    else:
        print('#{} 0'.format(t))