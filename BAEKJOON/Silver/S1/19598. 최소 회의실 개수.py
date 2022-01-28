from collections import deque

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
room.sort(key = lambda x : (x[0], -x[1]))
q = deque()
for r in room:
    q.append(r)
room_cnt = 1
start, end = q.popleft()
while q:
    s, e = q.pop()
    if s < end:
        room_cnt += 1

