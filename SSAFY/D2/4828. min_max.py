test = int(input())
for t in range(1,test+1):
    N = int(input())
    ai = list(map(int, input().split()))
    max_num = ai[0]
    min_num = ai[0]
    for i in range(N-1):
        if max_num <=ai[i+1]:
            max_num = ai[i+1]
        if min_num >=ai[i+1]:
            min_num = ai[i+1]
    print('#{0} {1}'.format(t, max_num-min_num))