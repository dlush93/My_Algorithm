M = int(input())
N = int(input())
result = []
for num in range(M, N + 1):
    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result.append(num)
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)