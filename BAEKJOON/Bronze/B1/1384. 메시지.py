cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    if cnt >= 1:
        print('')
    cnt += 1
    print(f'Group {cnt}')
    group = [list(input().split()) for i in range(n)]
    print(group)
    flag = True
    for idx1, ans in enumerate(group):
        for idx2, i in enumerate(ans[1:], 1):
            if i == 'N':
                flag = False
                print(f'{group[idx1-idx2][0]} was nasty about {ans[0]}')
    else:
        if flag:
            print("Nobody was nasty")