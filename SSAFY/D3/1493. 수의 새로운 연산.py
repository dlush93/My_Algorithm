test = int(input())
for t in range(1,test+1):
    p, q = map(int, input().split())
    a ,b ,c ,d ,e ,f = 1, 1, 0, 1, 1, 0
    for i in range(1,10001):
        if a <= p <= b:
            c = i
            break
        else:
            a = a + i
            b = b + i + 1
    new_p = []
    for j in range(c):
        if p == a + j:
            new_p = [j+1,c-j]

    for k in range(1,10001):
        if d <= q <= e:
            f = k
            break
        else:
            d = d + k
            e = e + k + 1
    new_q = []
    for l in range(f):
        if q == d + l:
            new_q = [l+1,f-l]

    result = [new_p[0] + new_q[0], new_p[1] + new_q[1]]
    result2 = int((sum(result)-1)*(sum(result)-2)/2 +result[0])
    print('#{} {}'.format(t, result2))