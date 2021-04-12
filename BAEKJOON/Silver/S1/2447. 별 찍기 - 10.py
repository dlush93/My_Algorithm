def recursion(num):
    global arr
    if num == N*3:
        return

    for i in range(0, N, num):
        for j in range(0, N, num):
            for k in range(num//3):
                arr[i+num//3+k][j+num//3:j+2*(num//3)] = [' ']*(num//3)

    return recursion(num*3)


N = int(input())
arr = [['*'] * N for i in range(N)]
recursion(3)
for i in arr:
    print(''.join(i))