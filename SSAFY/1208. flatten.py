for t in range(1, 11):
    work = int(input())
    box = list(map(int, input().split()))
    box.sort()
    for w in range(work):
        if max(box) == min(box):
            print('#{0} 0'.format(t))
            break
        elif max(box) == min(box)+1:
            print('#{0} 1'.format(t))
            break
        else:
            box[-1] = max(box)-1
            box[0] = min(box)+1
    print('#{0} {1}'.format(t, max(box)-min(box)))