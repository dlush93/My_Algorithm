from collections import deque

def melt(glacier):
    remain = set()

    for g in glacier:
        x, y = g
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == '.':
                    break
        else:
            remain.add((x, y))
    return remain


def move():
    q = deque()
    q.append(swan[0])
    visited = [[True for _ in range(C)] for _ in range(R)]
    visited[swan[0][0]][swan[0][1]] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny]:
                    visited[nx][ny] = False
                    if board[nx][ny] == 'L':
                        return True
                    elif board[nx][ny] ==
                    q.append([nx. ny])


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
swan = []
glacier = set()
for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            glacier.add((i, j))
        elif board[i][j] == 'L':
            swan.append((i, j))
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
print(swan)