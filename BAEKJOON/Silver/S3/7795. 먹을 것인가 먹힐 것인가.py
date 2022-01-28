import sys
input = sys.stdin.readline

for t in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())), reverse=True)
    cnt = 0
    for i in range(N):
        if A[i] > B[0]:
            cnt += (N-i)*M
            break
        for j in range(M):
            if A[i] > B[j]:
                cnt += M-j
                break
    print(cnt)