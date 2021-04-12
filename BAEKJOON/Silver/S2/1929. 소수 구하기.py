def prime_num():
    sieve = [True] * (N + 1)

    m = int((N + 1) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, N + 1, i):
                sieve[j] = False

    return [i for i in range(M, N+1) if sieve[i] == True]

M, N = map(int, input().split())
prime_list = prime_num()
for num in prime_list:
    if num >= 2:
        print(num)
