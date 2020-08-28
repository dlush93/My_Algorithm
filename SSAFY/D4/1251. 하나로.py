def min_length(line):

    temp = 10000000000000
    for i in range(line, N):
        if island[line] != island[i]:
            length = ((island[line][0]-island[i][0])**2 + (island[line][1]-island[i][1])**2)**(1/2)
            if length < temp:
                temp = length
    if temp == 10000000000000:
        return 0
    else:
        return round(E * (temp**2))

for t in range(1, int(input())+1):
    N = int(input())
    island = []
    x_value = list(map(int, input().split()))
    y_value = list(map(int, input().split()))
    for i in range(N):
        island.append([x_value[i], y_value[i]])
    E = float(input())
    min_len = 1000000000000
    cost = []
    for i in range(N):
        cost.append(min_length(i))
    print(sum(cost))
    # print('#{} {}'.format(t, cost))