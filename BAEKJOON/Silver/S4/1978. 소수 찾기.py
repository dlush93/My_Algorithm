N = int(input())
num_list = list(map(int, input().split()))
result = 0
for num in num_list:
    if num >= 2:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            result += 1
print(result)