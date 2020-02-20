def rps(a,b):
    if data[a] == data[b]:
        return a
    elif data[a] ==1:
        if data[b] == 2:
            return b
        elif data[b] == 3:
            return a
    elif data[a] ==2:
        if data[b] == 3:
            return b
        elif data[b] == 1:
            return a
    elif data[a] ==3:
        if data[b] == 1:
            return b
        elif data[b] == 2:
            return a


def tournament(i, j):
    if i == j:
        return i

    l = tournament(i, (i+j)//2)
    r = tournament((i+j)//2+1, j)

    return rps(l,r)


for t in range(1, int(input())+1):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    print('#{} {}'.format(t, tournament(1,N)))