R, C = map(int, input().split())
picture = [list(input()) for i in range(C)]
team = [0] * 9
rank = 1
chk = 0
ranking = [0] * 9
for p in picture:
    cnt = 0
    for i in p[::-1]:
        if not i.isdecimal():
            cnt += 1
        else:
            team[int(i)-1] = cnt
            break
while chk != 9:
    for i in range(9):
        