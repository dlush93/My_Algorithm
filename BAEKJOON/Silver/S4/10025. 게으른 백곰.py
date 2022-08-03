N, K = map(int, input().split())
ice = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
start, end, val = 0, 0, 0
result = 0
while end != N:
    if (ice[end][1] - ice[start][1])//2 <= 2*K:
        val += ice[end][0]
    else:
        result = max(result, val, ice[end][0])
        val -= ice[start][0]
        start += 1
    end += 1
print(result)