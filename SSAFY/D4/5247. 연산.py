from collections import deque

def operation(num, cnt):
    q = deque()
    q.append([num, cnt])
    while q:
        num, cnt = q.popleft()
        if num > 1000000 or num < 0:
            continue
        if num == M:
            return cnt
        if visit[num]:
            cnt +=1
            q.append([num+1, cnt])
            q.append([num-1, cnt])
            q.append([num*2, cnt])
            q.append([num-10, cnt])
            visit[num] = 0

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    visit = [1]*1000001
    result = operation(N, 0)
    print('#{} {}'.format(t, result))