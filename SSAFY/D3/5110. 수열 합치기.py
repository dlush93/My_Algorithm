for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M-1):
        data = list(map(int, input().split()))
        for j in range(len(arr)):
            if data[0] < arr[j]:
                arr = arr[:j] + data + arr[j:]
                break
        else:
            arr = arr + data
    print('#{} {}'.format(t, ' '.join(map(str, arr[-1:-11:-1]))))