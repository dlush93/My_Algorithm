import sys
input = sys.stdin.readline

N = int(input())
q = []
cnt = 0
for i in range(N):
    order = list(input().split())
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if len(q)-cnt:
            print(q[cnt])
            cnt += 1
        else:
            print(-1)
    elif order[0] == 'size':
        if cnt:
            print(len(q)-cnt)
        else:
            print(len(q))
    elif order[0] == 'empty':
        if len(q)-cnt:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(q)-cnt:
            print(q[cnt])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(q)-cnt:
            print(q[-1])
        else:
            print(-1)