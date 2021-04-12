def recursion(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return recursion(num-1) + recursion(num-2)

n = int(input())
print(recursion(n))