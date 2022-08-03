def backtracking(value, cnt):
    global max_value, min_value
    if cnt == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)

    if operators[0] > 0:
        operators[0] -= 1
        backtracking(value+num[cnt], cnt+1)
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        backtracking(value-num[cnt], cnt+1)
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        backtracking(value*num[cnt], cnt+1)
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        if value < 0:
            backtracking((value*-1)//num[cnt]*-1, cnt + 1)
        else:
            backtracking(value//num[cnt], cnt+1)
        operators[3] += 1


N = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_value, min_value = -1000000000, 1000000000
backtracking(num[0], 1)
print(max_value)
print(min_value)