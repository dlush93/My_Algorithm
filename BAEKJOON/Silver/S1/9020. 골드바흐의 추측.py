def prime_num(num):
    sieve = [True]*num
    sieve[1] = False
    m = int(num**0.5) + 1

    for i in range(2, m):
        if sieve[i] == True:
            for j in range(i+i, num, i):
                sieve[j] = False

    return [i for i in range(2, num) if sieve[i] == True]


def find_sum(find_num, find_list):
    chk_list = []
    mid_value = find_num//2
    min_dif = 10000
    if mid_value in find_list:
        return [mid_value, mid_value]
    min_index = 0
    max_index = len(find_list) - 1
    while min_index <= max_index:
        mid_index = (max_index + min_index)//2
        if find_list[mid_index] > mid_value:
            max_index = mid_index - 1
        elif find_list[mid_index] < mid_value:
            min_index = mid_index + 1

    while mid_index >= 0:
        other_num = find_value - find_list[mid_index]
        dif = abs(other_num - find_list[mid_index])
        if other_num in find_list:
            if min_dif > dif:
                min_dif = dif
                chk_list = [other_num, find_list[mid_index]]
                chk_list.sort()
        mid_index -= 1

    return chk_list

prime_list = prime_num(10000)
for t in range(int(input())):
    find_value = int(input())
    print(*find_sum(find_value, prime_list[0:find_value]))
