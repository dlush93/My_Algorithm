for t in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    stack = [data[0]]
    for i in range(1,N):
        if data[i] + stack[-1] >=0:
            stack.append(data[i] + stack[-1])
        else:
            stack.append(0)
    print('#{} {}'.format(t, max(stack)))