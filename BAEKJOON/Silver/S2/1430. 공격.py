tower, tower_range, energy, a_x, a_y = map(int, input().split())
data = []
for i in range(tower):
    x, y = map(int, input().split())
    data.append([x,y])
print(data)