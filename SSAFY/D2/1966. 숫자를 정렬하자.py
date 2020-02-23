for t in range(1, int(input())+1):
    input()
    data = list(map(int, input().split()))
    data.sort()
    print('#{} {}'.format(t, ' '.join(map(str, data))))