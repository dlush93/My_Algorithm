for t in range(int(input())):
    num = int(input())
    num_list = []
    for i in range(9, 1, -1):
        if num%i == 0:
            while num%i == 0:
                num_list.append(i)
                num = num//i
    if num != 1 and num >= 10:
        print(-1)
    elif len(num_list) == 0 and num == 1:
        print(1)
    else:
        print(len(num_list))