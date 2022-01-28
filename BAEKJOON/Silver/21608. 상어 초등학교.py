def location(num, cnt):
    if cnt == 0:
        table[N-1][N-1] = num

    if 

N = int(input())
like_num = dict()
order = []
table = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N*N):
    num = list(map(int, input().split()))
    like_num[num[0]] = set(num[1:])
    order.append(num[0])

for i in range(N*N):
    location(order[i], i)
