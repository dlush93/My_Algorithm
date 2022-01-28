from collections import deque

for t in range(int(input())):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))
    q.insert(M+1, 0)
    cnt = 0
    while True:
        q.rotate(-q.index(max(q)))
        q.popleft()
        cnt += 1
        if q[0] == 0:
            break
    print(cnt)