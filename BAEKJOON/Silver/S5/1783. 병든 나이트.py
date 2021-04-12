N, M = map(int, input().split())
knight = [1, 1]
cnt = 0
if M < 8:
    if N > M:
        while knight[0] <= N and knight[1] <= M:
            k