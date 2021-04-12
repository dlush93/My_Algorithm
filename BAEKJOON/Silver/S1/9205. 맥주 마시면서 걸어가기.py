def distance_chk(now, end):
    nx, ny = now
    ex, ey = end
    dx, dy = abs(nx-ex), abs(ny-ey)
    if (dx + dy)/50 > 20:
        return False
    else:
        if abs(rock_x-nx) + abs(rock_y-ny) < abs(rock_x-ex) + abs(rock_y-ey):
            return False
        else:
            return True


for t in range(int(input())):
    n = int(input())
    beer = 20
    arr = [[0]*65536 for i in range(65536)]
    store = []
    home_x, home_y = map(int, input().split())
    arr[home_x+32768][home_y+32768] = 1
    for i in range(n):
        x, y = map(int, input())
        store.append([x, y])
        arr[x+32768][y+32768] = 2
    rock_x, rock_y = map(int, input().split())
    arr[rock_x+32768][rock_y+32768] = 3