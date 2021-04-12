N = int(input())
cost = [list(map(int, input().split())) for i in range(N)]
min_cost = [cost[0]]
for i in range(1, N):
    red_cost = min(min_cost[i-1][1], min_cost[i-1][2]) + cost[i][0]
    green_cost = min(min_cost[i-1][2], min_cost[i-1][0]) + cost[i][1]
    blue_cost = min(min_cost[i-1][0], min_cost[i-1][1]) + cost[i][2]
    min_cost.append([red_cost, green_cost, blue_cost])
print(min(min_cost[N-1]))