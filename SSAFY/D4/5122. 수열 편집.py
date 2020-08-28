def ins(data):
    global arr
    space = int(data[1])
    num = int(data[2])
    head = arr[:space]
    tail = arr[space:]
    arr = head + [num] + tail

def dlt(data):
    global arr
    space = int(data[1])
    arr.pop(space)

def chg(data):
    global arr
    space = int(data[1])
    num = int(data[2])
    arr[space] = num


for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        data = list(input().split())
        if data[0] == 'I':
            ins(data)
        elif data[0] == 'D':
            dlt(data)
        else:
            chg(data)
    if L > len(arr):
        print('#{} -1'.format(t))
    else:
        print('#{} {}'.format(t, arr[L]))

