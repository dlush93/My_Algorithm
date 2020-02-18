import sys
for t in range(3):
    N = int(sys.stdin.readline())
    a = 0
    for i in range(N):
        a += int(sys.stdin.readline())
    if a > 0:
        print('+')
    elif a < 0:
        print('-')
    else:
        print('0')