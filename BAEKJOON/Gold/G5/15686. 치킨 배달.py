from collections import deque
from itertools import combinations


def chicken_distance(start, remain_chicken):
    x, y = start
    distance = N*N
    for remain in remain_chicken:
        cx, cy = remain
        distance = min(distance, abs(x-cx) + abs(y-cy))
    return distance


def close_chicken():
    result = 1000000000
    chicken_set = set(chicken)
    if len(chicken) > M:
        for comb in combinations(chicken, len(chicken)-M):
            distance = 0
            remain_chicken = chicken_set - set(comb)
            for h in home:
                distance += chicken_distance(h, remain_chicken)
            result = min(result, distance)
    else:
        distance = 0
        for h in home:
            distance += chicken_distance(h, chicken_set)
        result = min(result, distance)
    return result


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]
home = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
print(close_chicken())