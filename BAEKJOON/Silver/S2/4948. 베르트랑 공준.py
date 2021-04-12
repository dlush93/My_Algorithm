def prime_num(num):
    sieve = [True] * (2*num + 1)
    sieve[1] = False
    m = int((2*num + 1)**0.5) + 1
    for i in range(2, m):
        if sieve[i] == True:
            for j in range(i + i, 2 * num + 1, i):
                sieve[j] = False

    return [i for i in range(num + 1, 2*num+1) if sieve[i] == True]


num_list = []
while True:
    num_list.append(int(input()))
    if num_list[-1] == 0:
        break

for num in num_list[0:-1]:
    print(len(prime_num(num)))