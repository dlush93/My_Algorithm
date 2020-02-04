# arr = [list([i]*5) for i in range(1,6)]
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j])
#
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j])
#
N = int(input())
for i in range(1,N+1):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))