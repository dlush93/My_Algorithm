for t in range(1, int(input())+1):
    arr = [31,28,31,30,31,30,31,31,30,31,30,31]
    m1, d1, m2, d2 = map(int, input().split())
    print('#{} {}'.format(t, sum(arr[0:m2-1])+ d2 + 1 - sum(arr[0:m1-1])-d1))