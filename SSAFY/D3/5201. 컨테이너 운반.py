for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    result = 0
    weight.sort()
    truck.sort()
    while len(truck) != 0 and len(weight) != 0:
        a = weight.pop()
        b = truck.pop()
        if a <= b:
            result += a
        else:
            truck.append(b)
    print('#{} {}'.format(t, result))