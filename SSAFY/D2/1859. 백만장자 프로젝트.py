for t in range(1, int(input())+1):
    N = int(input())
    data = list(map(int,input().split()))
    stack =[]
    benefit = 0
    for i in range(N-1,-1,-1):
        if len(stack) ==0:
            stack.append(data[i])
        elif stack[0] > data[i]:
            benefit += stack[0] - data[i]
        elif stack[0] < data[i]:
            stack.pop()
            stack.append(data[i])
    print('#{} {}'.format(t, benefit))