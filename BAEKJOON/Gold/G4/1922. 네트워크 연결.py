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


N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]
result = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(a, parent) != find_parent(b, parent):
        result += cost
        union_parent(a, b, parent)
print(result)