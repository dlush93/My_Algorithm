for t in range(1, int(input())+1):
    N = int(input())
    data = [list(input().split()) for i in range(N)]
    arr = [[0]*N for i in range(N)]
    for i in range(3):
        result = []
        for j in range(N):
            for k in range(N):
                arr[j][k] = data[N-k-1][j]


# def angle(num, n):
#     arr = [[0]*n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] = num[n-j-1][i]
#     return arr
# test = int(input())
# for t in range(1,test+1):
#     N = int(input())
#     data = [list(input().split()) for i in range(N)]
#     result1 = angle(data, N)
#     result2 = angle(result1, N)
#     result3 = angle(result2, N)
#     print('#{}'.format(t))
#     result = ''
#     for i in range(N):
#         print(''.join(result1[i]) + ' ' + ''.join(result2[i]) + ' ' + ''.join(result3[i]))
