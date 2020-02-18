N = int(input())
data = [list(map(int,input().split())) for i in range(N)]
status = 0

MIN = 1000
for i in range(N):
    for j in range(i+1, N):
