tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    data = [input() for x in range(N)]
    arr = [0]*26
    for i in data:
        arr[ord(i[0]) - ord('A')] +=1
    j = 0
    cnt = 0
    while arr[j] != 0:
        if arr[j] >= 1:
            j +=1
            cnt +=1
        else:
            break
    print('#{} {}'.format(t, cnt))