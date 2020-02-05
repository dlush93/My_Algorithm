test = int(input())
for t in range(1, test+1):
    N = int(input())
    tc = list(map(int, input().split()))
    tc2 = [[tc[2*i],tc[2*i+1]] for i in range(N)]
    result = []
    result.append(tc2[0])
    count = 1
    j = 1
    ans = ''
    while count != N:
        if tc2[j][0] == result[-1][-1]:
            result.append(tc2[j])
            count +=1
        elif tc2[j][-1] == result[0][0]:
            result.insert(0, tc2[j])
            count +=1
        j +=1
        if j == N:
            j -= (N-1)
    for r in result:
        ans += ' ' + str(r[0]) + ' ' + str(r[-1])
    ans.rstrip()
    print('#{}{}'.format(t, ans))