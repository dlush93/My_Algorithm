def backtracking(num, cnt, pl, mi, mu, di):
    global max_num, min_num
    if pl + mi + mu + di == 0:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        return

    if pl > 0:
        backtracking(num+nums[cnt], cnt+1, pl-1, mi, mu, di)
    if mi > 0:
        backtracking(num-nums[cnt], cnt+1, pl, mi-1, mu, di)
    if mu > 0:
        backtracking(num*nums[cnt], cnt+1, pl, mi, mu-1, di)
    if di > 0:
        if num < 0:
            backtracking(((-1*num)//nums[cnt])*-1, cnt+1, pl, mi, mu, di-1)
        else:
            backtracking(num//nums[cnt], cnt + 1, pl, mi, mu, di - 1)


N = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
min_num = 1000000000
max_num = -1000000000
backtracking(nums[0], 1, plus, minus, mul, div)
if plus + minus + mul + div == 0:
    print(max(nums))
    print(min(nums))
else:
    print(max_num)
    print(min_num)