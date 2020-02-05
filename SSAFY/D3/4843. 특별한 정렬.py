test = int(input())
for t in range(1, test+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    result = ''
    count = 0
    for n in range(N):
        if n%2 == 0:
            result += str(data[N-1-n//2]) + ' '
            count +=1
        else:
            result += str(data[n//2]) + ' '
            count +=1
        if count ==10:
            break
    result.rstrip()
    print('#{} {}'.format(t, result))