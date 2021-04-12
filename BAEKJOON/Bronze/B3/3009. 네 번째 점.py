x_list = []
y_list = []
sum_x = 0
sum_y = 0
for i in range(3):
    x, y = map(int, input().split())
    if x not in x_list:
        x_list.append(x)
        sum_x += x*2
    if y not in y_list:
        y_list.append(y)
        sum_y += y*2
    sum_x -= x
    sum_y -= y
print(sum_x, sum_y)
