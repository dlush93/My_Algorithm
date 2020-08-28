def price(idx, num):
    global min_price

    if min_price < num:
        return
    if idx == N:
        if num < min_price:
            min_price = num
            return
    else:
        for i in range(N):
            if selected[i] == 0 :
                selected[i] = 1
                num += data[idx][i]
                price(idx+1, num)
                num -= data[idx][i]
                selected[i] = 0



for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    selected = [0]*N
    min_price = 99*15*15
    price(0, 0)
    print('#{} {}'.format(t, min_price))
