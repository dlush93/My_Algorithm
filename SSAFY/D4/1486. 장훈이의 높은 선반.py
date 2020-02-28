from itertools import combinations

for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    min_num = 1000000000
    for i in range(1,N+1):
        com = combinations(data,i)
        for j in com:
            if sum(j) >= B:
                min_num = min(min_num, abs(B-sum(j)))
    print('#{} {}'.format(t, min_num))