def recursion(num, start, end):
    if num == 1:
        print(start, end)
        return

    recursion(num-1, start, 6-start-end)
    print(start, end)
    recursion(num-1, 6-start-end, end)


N = int(input())
print(2**N - 1)
recursion(N, 1, 3)