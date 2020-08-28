for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    pizza=[]
    hwaduck = []
    n = 0
    for i in range(1, M+1):
        pizza.append([i,data.pop(0)])
    for i in range(N):
        hwaduck.append(pizza.pop(0))
    while n != M-1 :
        cheese = hwaduck.pop(0)
        cheese[-1] = cheese[-1]//2
        if cheese[-1] == 0 and len(pizza) !=0 :
            hwaduck.append(pizza.pop(0))
            n += 1
        elif cheese[-1] ==0:
            n += 1
        else:
            hwaduck.append(cheese)
    for h in hwaduck:
        if h[-1] != 0:
            print('#{} {}'.format(t, h[0]))
            break