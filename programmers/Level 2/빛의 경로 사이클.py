def solution(grid):
    answer = []
    route = [[[0 for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for d in range(4):
                if route[x][y][d]:
                    continue
                cnt = 0
                while not route[x][y][d]:
                    route[x][y][d] = 1
                    if grid[x][y] == 'L':
                        d = (d+1)%4
                    elif grid[x][y] == 'R':
                        d = (d-1)%4
                    x, y = (x+dx[d])%len(grid), (y+dy[d])%len(grid[0])
                    cnt += 1
                answer.append(cnt)
    return sorted(answer)

print(solution(["SL","LR"]))
print(solution([["S"]]))
print(solution(["R","R"]))