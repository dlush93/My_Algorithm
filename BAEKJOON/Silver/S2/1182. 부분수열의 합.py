import sys
input = sys.stdin.readline


def part_sum(value, k):
    global cnt
    if k == N:
        if value == S:
            cnt += 1
    else:
        part_sum(value+array[k], k+1)
        part_sum(value, k+1)


N, S = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0
part_sum(0, 0)
if S == 0:
    cnt -= 1
print(cnt)