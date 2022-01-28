from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[1 for _ in range(m)] for _ in range(n)]

    def bfs(start):
        q = deque()
        q.append(start)

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and visited[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    if nx == n-1 and ny == m-1:
                        return
        else:
            visited[n-1][m-1] = -1

    bfs((0, 0))
    answer = visited[n-1][m-1]

    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])