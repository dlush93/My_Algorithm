def recursion(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num*recursion(num-1)

N = int(input())
print(recursion(N))