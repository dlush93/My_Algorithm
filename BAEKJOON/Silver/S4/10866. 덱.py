import sys, time
input = sys.stdin.readline
front_idx = 0
back_idx = -1
length = 0
q = []
for i in range(int(input())):
    order = list(input().split())
    if order[0] == 'push_front':
        q.insert(front_idx, order[1])
        length += 1
    elif order[0] == 'push_back':
        q.insert(back_idx, order[1])
        length += 1
    elif order[0] == 'pop_front':
        if length:
            print(q[front_idx])
            front_idx += 1
            length -= 1
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if length:
            print(q[back_idx])
            back_idx -= 1
            length -= 1
        else:
            print(-1)
    elif order[0] == 'size':
        print(length)
    elif order[0] == 'empty':
        if length:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if length:
            print(q[front_idx])
        else:
            print(-1)
    elif order[0] == 'back':
        if length:
            print(q[back_idx])
        else:
            print(-1)