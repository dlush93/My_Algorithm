from collections import deque

N, K = map(int, input().split())
num_list = deque(range(1, N+1))
arr = []
while num_list:
    num_list.rotate(-K)
    arr.append(num_list.pop())

print('<' + ', '.join(map(str, arr)) + '>')
