test = int(input())
for t in range(1,test+1):
    arr = [0] * 101
    input()
    data = list(map(int, input().split()))
    for i in data:
        arr[i] += 1
    for idx, j in list(enumerate(arr))[::-1]:
        if j == max(arr):
            print('#{} {}'.format(t, idx))
            break