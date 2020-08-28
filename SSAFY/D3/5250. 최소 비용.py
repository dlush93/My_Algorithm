from collections import deque
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(start, fuel):
    q = deque()
    q.append(start)

    




for t in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    visit = [[0]*N for i in range(N)]
