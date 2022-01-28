from collections import Counter

N = int(input())
nums = Counter([int(input()) for i in range(N)])
min_num, max_cnt = 2**62, 0
for num, cnt in nums.items():
    if cnt > max_cnt:
        max_cnt = cnt
        min_num = num
    elif cnt == max_cnt:
        min_num = min(min_num, num)
print(min_num)