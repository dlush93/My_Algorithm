for t in range(int(input())):
    N = int(input())
    fibo_zero = [1, 0]
    fibo_one = [0, 1]
    for i in range(2, N+1):
        fibo_zero.append(fibo_zero[i-1]+fibo_zero[i-2])
        fibo_one.append(fibo_one[i-1]+fibo_one[i-2])
    print(fibo_zero[N], fibo_one[N])