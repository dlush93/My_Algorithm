N = int(input())
room = 2
room_min = 2
room_max = 1
for i in range(1, 1000000000):
    if N == 1:
        print(1)
        break
    else:
        room_min += 6*(i-1)
        room_max += 6*i
        if room_min <= N <= room_max:
            print(room)
            break
        else:
            room +=1