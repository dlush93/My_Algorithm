N, M, K = map(int, input().split())
genre = [list(input().split()) for i in range(M)]
people = [[] for i in range(N)]
point = []
for g in genre:
    for i in range(N):
        people[int(g[i*2])-1].append(float(g[i*2+1]))
for p in people:
    point.append(max(p))
result = sum(sorted(point, reverse=True)[:K])
print('%.1f' % result)