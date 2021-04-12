N, M = map(int, input().split())
chess = [list(input()) for i in range(N)]
min_cnt = 64
bow1 = [ord('W'), ord('B')]
bow2 = [ord('B'), ord('W')]
for i in range(N-7):
    for j in range(M-7):
        row = 0
        col = 0
        cnt1 = 0
        cnt2 = 0
        while col != 8:
            if ord(chess[i+col][j+row]) != bow1[(col+row)%2]:
                cnt1 += 1
            if ord(chess[i+col][j+row]) != bow2[(col+row)%2]:
                cnt2 += 1
            if row < 7:
                row += 1
            else:
                row = 0
                col += 1
            if min(cnt1, cnt2) >= min_cnt:
                break
        if min(cnt1, cnt2) < min_cnt:
            min_cnt = min(cnt1, cnt2)
print(min_cnt)