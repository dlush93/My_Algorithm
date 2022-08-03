from collections import deque


def wheel_rotate(num, direc): #2오른쪽,6왼쪽
    rotate_chk = []
    for i in range(3):
        if wheel_list[i][2] != wheel_list[i+1][6]:
            rotate_chk.append(1)
        else:
            rotate_chk.append(0)
    if num == 0:
        start = 0
        wheel_list[num].rotate(direc)
        direc *= -1
        while start < 3 and rotate_chk[start]:
            wheel_list[start+1].rotate(direc)
            direc *= -1
            start += 1
    elif num == 3:
        start = 2
        wheel_list[num].rotate(direc)
        direc *= -1
        while start >= 0 and rotate_chk[start]:
            wheel_list[start].rotate(direc)
            direc *= -1
            start -= 1
    else:
        left, right = num-1, num
        wheel_list[num].rotate(direc)
        left_d, right_d = direc*-1, direc*-1
        while right < 3 and rotate_chk[right]:
            wheel_list[right+1].rotate(right_d)
            right_d *= -1
            right += 1
        while left >= 0 and rotate_chk[left]:
            wheel_list[left].rotate(left_d)
            left_d *= -1
            left -= 1


wheel_list = [deque(list(map(int, list(input())))) for _ in range(4)]
for t in range(int(input())):
    wheel, direction = map(int, input().split())
    wheel_rotate(wheel-1, direction)
print(wheel_list[0][0]*1+wheel_list[1][0]*2+wheel_list[2][0]*4+wheel_list[3][0]*8)