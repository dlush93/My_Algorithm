test = int(input())
for t in range(1,test+1):
    N = int(input())
    data = list(map(int, input().split()))
    arr = []
    for i in range(N):
        for j in range(i+1,N):
            a = str(data[i]*data[j])
            b = True
            for k in range(len(a)-1):
                if a[k] > a[k+1]:
                    b=False
                    break
            if b:
                arr.append(int(a))
    if arr == []:
        print('#{} -1'.format(t))
    else:
        print('#{} {}'.format(t,max(arr)))




# test = int(input())
# # for t in range(1, test+1):
# #     N = int(input())
# #     data = list(map(int,input().split()))
# #     arr = []
# #     for i in range(N):
# #         for j in range(i+1,N):
# #             ans = data[i]*data[j]
# #             for i in range(len(str(ans))-1):
# #                 if int(str(ans)[i]) > int(str(ans)[i + 1]):
# #                     break
# #             else:
# #                 arr.append(ans)
# #     if N == 1:
# #         print('#{} {}'.format(t, data[0]))
# #         break
# #     else:
# #         print('#{} {}'.format(t, max(arr)))
