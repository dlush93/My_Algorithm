import sys
input = sys.stdin.readline


def comb_sum(num1, num2):
    new_nums = dict()
    for i in range(n):
        for j in range(n):
            if nums[i][num1] + nums[j][num2] not in new_nums:
                new_nums[nums[i][num1] + nums[j][num2]] = 0
            new_nums[nums[i][num1] + nums[j][num2]] +=1
    return new_nums


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
dict1 = comb_sum(0, 1)
result = 0
for i in range(n):
    for j in range(n):
        if (nums[i][2] + nums[j][3])*-1 in dict1:
            result += dict1[(nums[i][2] + nums[j][3])*-1]
print(result)