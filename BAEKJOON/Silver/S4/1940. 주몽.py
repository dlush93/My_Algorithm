N = int(input())
M = int(input())
material = sorted(list(map(int, input().split())))
start, end, cnt = 0, N-1, 0
while start < end:
    if material[start] + material[end] > M:
        end -= 1
    elif material[start] + material[end] < M:
        start += 1
    else:
        start += 1
        end -= 1
        cnt += 1
print(cnt)