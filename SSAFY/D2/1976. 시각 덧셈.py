for t in range(1, int(input())+1):
    h1, m1, h2, m2= map(int, input().split())
    H = h1 + h2
    M = m1 + m2
    if M >= 60:
        H +=1
        M -= 60
    if H >= 12:
        H -= 12
    print('#{} {} {}'.format(t, H, M))