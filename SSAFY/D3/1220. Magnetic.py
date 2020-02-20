for t in range(1, 11):
    input()
    cnt = 0
    data = [list(map(int, input().split())) for i in range(100)]
    for i in range(100):
        n = 0
        stack = []
        while n < 100:
            if data[n][i] == 0:
                n += 1
            elif data[n][i] == 1:
                stack.append(1)
                n += 1
            else:
                if len(stack) == 0:
                    n += 1
                elif stack[-1] == 1:
                    stack = []
                    cnt += 1
    print('#{} {}'.format(t, cnt))