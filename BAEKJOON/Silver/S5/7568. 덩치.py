N = int(input())
physical = [list(map(int, input().split())) for i in range(N)]
rank = [1]*N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if physical[i][0] < physical[j][0] and physical[i][1] < physical[j][1]:
            rank[i] += 1
print(' '.join(map(str, rank)))