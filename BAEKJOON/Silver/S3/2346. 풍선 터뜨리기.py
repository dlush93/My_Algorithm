from collections import deque

N = int(input())
balloons = list(map(int, input().split()))
q = deque()
for i in range(1, N+1):
    q.append([i, balloons[i-1]])
result = []
while q:
    balloon = q.popleft()
    result.append(balloon[0])
    if balloon[1] > 0:
        q.rotate(-balloon[1]+1)
    else:
        q.rotate(-balloon[1])
print(*result)