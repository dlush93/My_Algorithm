N, K = map(int, input().split())
arr = list(map(int, input().split()))
start, end, cnt = 0, 0, 0
result = 0
while end != N:
    if arr[end]%2:
        cnt += 1
        if cnt > K:
            result = max(result, end-start-K)
            while cnt > K:
                if arr[start]%2:
                    cnt -= 1
                start += 1
    end += 1
if cnt <= K:
    result = max(result, end-start-cnt)
print(result)