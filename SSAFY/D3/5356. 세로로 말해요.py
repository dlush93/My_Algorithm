test = int(input())
for t in range(1, test+1):
    data = [input() for i in range(5)]
    arr = [['.']*15 for i in range(15)]
    text = ''
    for i in range(5):
        for j in range(len(data[i])):
            arr[j][i] = data[i][j]
    for k in range(15):
        for l in range(15):
            if arr[k][l] !='.':
                text+=arr[k][l]
    print('#{} {}'.format(t, text))