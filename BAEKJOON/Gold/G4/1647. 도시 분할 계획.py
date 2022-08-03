import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edge = [list(map(int, input().split())) for _ in range(M)]
edge.sort(key=lambda x: x[2])
result = 0
max_cost = 0
for e in edge:
    a, b, c = e
    if find_parent(a, parent) != find_parent(b, parent):
        union_parent(a, b, parent)
        result += c
        max_cost = max(max_cost, c)
print(result-max_cost)