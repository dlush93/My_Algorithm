import sys
N = int(sys.stdin.readline())
book = [int(sys.stdin.readline()) for i in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if book[i] == N:
        N -= 1
    else:
        cnt += 1
print(cnt)