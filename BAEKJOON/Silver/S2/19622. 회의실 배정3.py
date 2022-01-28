N = int(input())
conf = [list(map(int, input().split())) for _ in range(N)]
conf.sort(key=lambda x:(x[1], x[0], -x[2]))
end = 0
start = 0
for time in conf:
    