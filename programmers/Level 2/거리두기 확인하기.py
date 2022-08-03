from collections import deque


def solution(places):
    answer = []
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    def bfs(start):
        q = deque()
        q.append([start[0], start[1], 0])
        visited = [[0 for _ in range(5)] for _ in range(5)]
        visited[start[0]][start[1]] = 1
        while q:
            x, y, cnt = q.popleft()
            if cnt == 2:
                continue
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        if place[nx][ny] == 'O':
                            q.append([nx, ny, cnt+1])
                        elif place[nx][ny] == 'P':
                            return False
        return True

    for place in places:
        candidate = []
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs([i, j]):
                        flag = False
                        break
            if not flag:
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))