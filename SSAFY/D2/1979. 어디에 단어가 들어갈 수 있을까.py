test = int(input())
for t in range(1, test+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) + [0] for i in range(N)] + [[0]*(N+1)]
    c = []
    for i in range(N+1):
        a,b,d,e = 0,0,0,0
        while a != N:
            if data[i][a] == 1:
                b += 1
                a += 1
            else:
                c.append(b)
                b = 0
                a +=1
        print(c)
        while d != N:
            if data[d][i] == 1:
                e += 1
                d += 1
            else:
                c.append(e)
                e = 0
                d +=1
    print('#{} {}'.format(t, c.count(K)))

# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, K = list(map(int, input().split()))  # N 행렬 크기 K 단어 크기
#     arr = [list(map(int, input().split())) for n in range(N)]
#     j = 0
#     result = 0
#     for i in range(N):
#         blank_cnt = 0
#         blank_cnt2 = 0
#         for j in range(N):
#             if arr[i][j] == 0:
#                 if blank_cnt == K:
#                     result += 1
#                 blank_cnt = 0
#             else:
#                 blank_cnt += 1
#                 if j == N - 1 and blank_cnt == K:
#                     result += 1
#
#             if arr[j][i] == 0:
#                 if blank_cnt2 == K:
#                     result += 1
#                 blank_cnt2 = 0
#             else:
#                 blank_cnt2 += 1
#                 if j == N - 1 and blank_cnt2 == K:
#                     result += 1
#     print('#{} {}'.format(test_case, result))