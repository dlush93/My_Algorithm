from collections import deque


def find_passenger(start):
    x, y = start
    q = deque()
    q.append([x, y, 0])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    stack = []
    distance = 5000000
    if MAP[x][y] > 1:
        return x, y, 0, MAP[x][y]
    while q:
        x, y, used = q.popleft()
        if used > distance:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if MAP[nx][ny] > 1:
                        distance = used
                        stack.append([nx, ny, used+1, MAP[nx][ny]])
                    elif MAP[nx][ny] != 1 and used < distance:
                        q.append([nx, ny, used+1])
    if len(stack) == 0:
        return x, y, 5000001, 0
    stack.sort(key=lambda x: (x[0], x[1]))
    return stack[0][0], stack[0][1], stack[0][2], stack[0][3]


def start_to_end(start, passenger):
    x, y = start
    q = deque()
    q.append([x, y, 0])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while q:
        x, y, used = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if nx == end_point[passenger][0] and ny == end_point[passenger][1]:
                        return nx, ny, used+1
                    elif MAP[nx][ny] != 1:
                        q.append([nx, ny, used+1])
    return x, y, 5000001


N, M, fuel = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
x, y = x-1, y-1
end_point = dict()
for i in range(2, M+2):
    sx, sy, ex, ey = map(int, input().split())
    MAP[sx-1][sy-1] = i
    end_point[i] = [ex-1, ey-1]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
for i in range(M):
    nx, ny, used_fuel, passenger = find_passenger([x, y])
    MAP[nx][ny] = 0
    fuel -= used_fuel
    if fuel < 0:
        print(-1)
        break
    x, y, used_fuel = start_to_end([nx, ny], passenger)
    fuel -= used_fuel
    if fuel < 0:
        print(-1)
        break
    else:
        fuel += used_fuel*2
else:
    print(fuel)