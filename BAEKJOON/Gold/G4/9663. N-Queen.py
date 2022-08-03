def backtracking(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        if chk[col] + left[row+col] + right[N-1+row-col] == 0:
            chk[col], left[row+col], right[N-1+row-col] = 1, 1, 1
            backtracking(row+1)
            chk[col], left[row+col], right[N-1+row-col] = 0, 0, 0


N = int(input())
cnt = 0
chk = [0 for _ in range(N)]
left, right = [0 for _ in range(2*N-1)], [0 for _ in range(2*N-1)]
backtracking(0)
print(cnt)