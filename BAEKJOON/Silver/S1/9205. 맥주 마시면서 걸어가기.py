def most_nearest_conven():
    near_distance = 1000
    near_con = []
    for con in conven:
        if abs(now[0] - con[0]) + abs(now[1] - con[1]) < near_distance:
            near_con.append([con[0], con[1]])


for t in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    now = [i for i in home]
    conven = set(tuple(map(int, input().split())) for i in range(n))
    rock = list(map(int, input().split()))
    distance = abs(home[0] - rock[0]) + abs(home[1] - rock[1])
    if distance <= 1000:
        print('happy')
    else:
        pass

