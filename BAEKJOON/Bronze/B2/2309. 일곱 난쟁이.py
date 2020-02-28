def dfs(cnt, total):
    global stack
    if total < 100:
        return
    if cnt ==9 and sum(stack) ==100:
        return

    for i in range(9):
        if arr[i] == 0:
            arr[i] = 1
            stack.append(data[i])
            dfs(cnt + 1, total + data[cnt][i])
            arr[i] = 0

data = [int(input()) for i in range(9)]
arr = [0]*9
stack = []
dfs(0,0)
print(stack)