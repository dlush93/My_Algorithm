# for t in range(int(input())):
#     H, W, N = map(int, input().split())
#     cnt = 1
#     result = []
#     for i in range(1, W+1):
#         if len(result) != 0:
#             break
#         for j in range(1, H+1):
#             if cnt == N:
#                 result.append(j)
#                 result.append(i)
#                 break
#             else:
#                 cnt += 1
#     if result[1] < 10:
#         print(f'{result[0]}0{result[1]}')
#     else:
#         print(f'{result[0]}{result[1]}')

for t in range(int(input())):
    H, W, N = map(int, input().split())
    print(((N-1)%H+1)*100 + (N-1)//H+1)