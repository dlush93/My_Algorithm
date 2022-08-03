import sys

N, X = map(int, input().split())
visitor = list(map(int, input().split()))
val = sum(visitor[:X])
max_visitor = sum(visitor[:X])
cnt = 1
start, end = 0, X
while end != N:
    val += visitor[end]
    val -= visitor[start]
    if val > max_visitor:
        max_visitor = val
        cnt = 1
    elif val == max_visitor:
        cnt += 1
    start += 1
    end += 1
if not max_visitor:
    print('SAD')
else:
    print(max_visitor)
    print(cnt)