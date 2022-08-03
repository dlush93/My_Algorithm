def backtracking(cnt, num):
    global min_click
    if cnt == 6 or cnt > len(str(N))+1:
        return
    for b in button:
        temp = num + str(b)
        min_click = min(min_click, len(temp) + abs(N-int(temp)))
        backtracking(cnt+1, temp)


N = int(input())
M = int(input())
button = set(range(10))
if M != 0:
    button -= set(map(int, input().split()))
min_click = abs(N - 100)
backtracking(0, '')
print(min_click)