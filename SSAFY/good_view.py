for test in range(1,11):
    width = int(input())
    building = list(map(int, input().split()))
    good_view = 0
    for i in range(width):
        if building[i] ==0:
            continue
        if building[i] > building[i-2] and building[i] > building[i-1] and building[i]>building[i+1] and building[i]>building[i+2]:
            good_view += building[i] - max(building[i-2],building[i-1],building[i+1],building[i+2])
    print('#{0} {1}'.format(test, good_view))