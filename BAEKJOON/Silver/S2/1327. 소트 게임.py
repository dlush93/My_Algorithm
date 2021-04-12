from collections import deque
import sys


def bfs(start, cnt):
    q = deque()
    q.append(start)
    chk = [start]
    while q:
        node = q.popleft()
        if node == match:
            return cnt

        for i in range(N-K+1):
            rev = node[i:i+K]
            rev = rev[::-1]
            node[i:i+K] = rev
            if node not in chk:
                chk.append(node)
                cnt += 1
                bfs(node, cnt)
    else:
        return -1


input = sys.stdin.readline
N, K = map(int, input().split())
data = list(map(int, input().split()))
match = sorted(data)
print(bfs(data, 0))