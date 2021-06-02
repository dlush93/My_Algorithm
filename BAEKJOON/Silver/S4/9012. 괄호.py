for t in range(int(input())):
    data = list(input())
    open = []
    for d in data:
        if d == '(':
            open.append(d)
        else:
            if len(open) == 0:
                print('NO')
                break
            else:
                open.pop()
    else:
        if len(open) == 0:
            print('YES')
        else:
            print('NO')