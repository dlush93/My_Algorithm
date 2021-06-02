import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    orders = list(input().split())
    if len(orders) == 2:
        stack.append(int(orders[1]))
    else:
        if orders[0] == 'pop':
            try:
                print(stack[-1])
                del stack[-1]
            except IndexError:
                print(-1)
        elif orders[0] == 'size':
            print(len(stack))
        elif orders[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif orders[0] == 'top':
            try:
                print(stack[-1])
            except IndexError:
                print(-1)