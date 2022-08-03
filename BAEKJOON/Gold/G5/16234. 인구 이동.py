from collections import deque
import sys
sys.setrecursionlimit(2001)


def union_nation(now_map, cnt):
    new_map = [m[:] for m in now_map]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                nations = [[i, j]]
                q.append([i, j])
                population = now_map[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[nx][ny] == 0:
                                if L <= abs(now_map[x][y] - now_map[nx][ny]) <= R:
                                    visited[nx][ny] = 1
                                    population += now_map[nx][ny]
                                    nations.append([nx, ny])
                                    q.append([nx, ny])
                aver_pop = int(population/len(nations))
                for nation in nations:
                    new_map[nation[0]][nation[1]] = aver_pop
    if now_map == new_map:
        return cnt
    else:
        now_map = new_map
        return union_nation(now_map, cnt + 1)


N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
print(union_nation(MAP, 0))