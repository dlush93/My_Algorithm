N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0
now_cost = cost[0]
for i in range(N-1):
    if now_cost > cost[i]:
        now_cost = cost[i]
    result += distance[i]*now_cost
print(result)