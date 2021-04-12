N = int(input())
meeting = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x:(x[1], x[0]))
cnt = 0
end = 0
for s, e in meeting:
    if s >= end:
        cnt += 1
        end = e
print(cnt)