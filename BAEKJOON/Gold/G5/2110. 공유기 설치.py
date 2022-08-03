def set_wifi(dist):
    wifi = house[0]
    cnt = 0
    for i in range(1, N):
        if house[i] >= wifi + dist:
            cnt += 1
            wifi = house[i]
    return False if cnt <= C else True


def binary_search():
    left = house[0]
    right = house[-1]

    while left <= right:
        mid = (left + right)//2
        print(left, right, mid)
        if set_wifi(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])
print(binary_search())