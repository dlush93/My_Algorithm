def search(cnt):
    global minimum
    if cnt == N:
        temp = 0
        for i in range(N):
            if select[i] == True:
                temp += height[i]
        if temp >= B:
            if temp < minimum:
                minimum = temp
        return
    select[cnt] = True
    search(cnt + 1)
    select[cnt] = False
    search(cnt + 1)


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    select = [False] * N
    print(len(select))
    minimum = sum(height) + 1
    search(0)

    print(f'#{t + 1} {minimum - B}')