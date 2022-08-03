import sys
from collections import deque
input = sys.stdin.readline

front, back = 0, 0
deque = [None for _ in range(10000)]
for i in range(int(input())):
    order = list(input().split())
    if order[0] == 'push_front':
        if deque[front]:
            front -= 1
        deque[front] = order[1]
    elif order[0] == 'push_back':
        if deque[back]:
            back += 1
        deque[back] = order[1]
    elif order[0] == 'pop_front':
        if deque[front]:
            print(deque[front])
            deque[front] = None
            front += 1
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if deque[back]:
            print(deque[back])
            deque[back] = None
            back -= 1
        else:
            print(-1)
    elif order[0] == 'size':
        print(back-front)
    elif order[0] == 'empty':
        if front == back:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if deque[front]:
            print(deque[front])
        else:
            print(-1)
    elif order[0] == 'back':
        if deque[back]:
            print(deque[back])
        else:
            print(-1)