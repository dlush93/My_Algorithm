for t in range(int(input())):
    H, W, N = map(int, input().split())
    arr = []
    n = 2
    for i in range(1,H+1):
        room = 1
        while room < n:
            floor = n
            ans = [floor-room, room]
            arr.append(ans)
            floor = floor - room
            room +=1
        n +=1
    for j in range(H+1, W+1):
        room = j - H +1
        floor = H
        while room < n :
            ans = [floor, room]
            arr.append(ans)
            room +=1
            floor -=1
        n +=1
    print(arr)