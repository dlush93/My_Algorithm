for t in range(int(input())):
    H, W, N = map(int, input().split())
    arr = []
    n = 2
    floor = 1
    room = 1
    while floor + room <= H + W:
        for i in range(floor+room-1, 0, -1):
            arr.append([i, room])
