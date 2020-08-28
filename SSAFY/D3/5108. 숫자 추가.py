def node(place, num):
    global arr
    head = arr[:place]
    tail = arr[place:]
    arr = head+[num]+tail
    return arr

for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        place, num = map(int,input().split())
        node(place, num)
    print('#{} {}'.format(t, arr[L]))