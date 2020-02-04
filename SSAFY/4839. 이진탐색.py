test = int(input())
for t in range(1, test+1):
    P, Pa, Pb = map(int, input().split())
    pa = pb = P
    l = 1
    C = int((P+l)/2)
    count_a = 0
    count_b = 0
    while C != Pa:
        if C < Pa:
            l = C
            C = int((C+pa)/2)
            count_a +=1
        elif C > Pa:
            pa = C
            C = int((l+C)/2)
            count_a +=1
    l = 1
    C = int((P+l)/2)
    while C != Pb:
        if C < Pb:
            l = C
            C = int((C+pb)/2)
            count_b +=1
        elif C > Pb:
            pb = C
            C = int((l+C)/2)
            count_b +=1
    if count_a > count_b:
        print('#{} B'.format(t))
    elif count_a < count_b:
        print('#{} A'.format(t))
    else:
        print('#{} 0'.format(t))