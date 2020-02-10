for t in range(1, int(input())+1):
    tc, N = map(str, input().split())
    data = list(input().split())
    a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = [0]*10
    for i in range(10):
        result[i] = data.count(a[i])
    print(tc)
    for j in range(10):
        print((a[j] + ' ')*result[j],end='')
    print()