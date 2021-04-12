def make_self_num():
    num_list = list(range(1, 20000))
    for i in range(1, 10000):
        now = str(i)
        new_num = i
        for j in range(len(now)):
            new_num += int(now[j])
        num_list[new_num - 1] = 0
    return num_list


for num in make_self_num():
    if num < 10000 and num != 0:
        print(num)
