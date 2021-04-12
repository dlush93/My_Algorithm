case = 1
while True:
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    use = (V//P)*L
    use += min(V%P, L)
    print(f'Case {case}: {use}')
    case +=1