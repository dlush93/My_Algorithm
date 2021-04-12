import sys
input = sys.stdin.readline


def backtracking(col):
    global result
    if col == N:
        result += 1
        return

    for i in range(N):
        if row[i] + left[i+col] + right[N-1+col-i] == 0:
            row[i] = left[i+col] = right[N-1+col-i] = 1
            backtracking(col+1)
            row[i] = left[i+col] = right[N-1+col-i] = 0


N = int(input())
row, left, right = [0]*N, [0]*(2*N-1), [0]*(2*N-1)
result = 0
backtracking(0)
print(result)