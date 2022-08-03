def binary_search(num):
    left = 0
    right = N-1
    if num < num_list[0] or num > num_list[-1]:
        return 0

    while left < right:
        mid = (left + right)//2
        if num_list[mid] < num:
            left = mid + 1
        else:
            right = mid
    mid = (left + right)//2
    return 1 if num_list[mid] == num else 0


N = int(input())
num_list = sorted(list(map(int, input().split())))
M = int(input())
find_list = list(map(int, input().split()))
for find_num in find_list:
    print(binary_search(find_num))