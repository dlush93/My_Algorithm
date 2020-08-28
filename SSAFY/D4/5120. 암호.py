for t in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    m = M
    for i in range(K):

        head = arr[:M]
        tail = arr[M:]
        arr = head+ [head[-1]+tail[0]]+tail
        print(arr)
        if M+m >= len(arr):
            M = M + m - len(arr)
        else:
            M = M + m
        print(M)
    print(arr)