N = int(input())
data = [[0,0]] + [list(map(int, input().split())) for i in range(N)]
max_benefit = 0
for i in range(1, N+1):