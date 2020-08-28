def find(list, r, key):
    l = 0
    d = -1
    while l <= r:
        m = (l+r)//2
        if key == list[m]:
            return 1
        elif key < list[m] and d != 0:
            r = m - 1
            d = 0
        elif key > list[m] and d != 1:
            l = m + 1
            d = 1
        else:
            return 0


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    list_A.sort()
    cnt = 0
    for key in list_B:
        if key in list_A:
            cnt += find(list_A, N-1, key)
    print('#{} {}'.format(t, cnt))