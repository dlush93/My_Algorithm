def binary_search():
    left = 1
    right = max(lines)
    length = 0
    while left <= right:
        mid = (left + right)//2

        if sum([line//mid for line in lines]) >= N:
            length = mid
            left = mid + 1
        else:
            right = mid - 1
    return length


K, N = map(int, input().split())
lines = list(int(input()) for _ in range(K))
print(binary_search())