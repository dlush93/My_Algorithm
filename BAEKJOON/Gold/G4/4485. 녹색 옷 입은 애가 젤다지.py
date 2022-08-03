import sys
import heapq
input = sys.stdin.readline


def dijkstra():
    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    q = []
    heapq.heappush(q, [0, 0, board[0][0]])
    distance[0][0] = 0

    while q:
        x, y, cost = heapq.heappop(q)

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                now_cost = cost + board[nx][ny]
                if now_cost < distance[nx][ny]:
                    distance[nx][ny] = now_cost
                    heapq.heappush(q, [nx, ny, now_cost])
    return distance[N-1][N-1]


cnt = 0
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

while True:
    N = int(input())
    if not N:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt += 1
    print(f'Problem {cnt}: {dijkstra()}')