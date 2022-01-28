N = int(input())
tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = list(map(int, input().split()))
    tree[b].append(a)
    tree[a].append(b)
for i in range(int(input())):
    num1, num2 = map(int, input().split())
    tree_set1 = set(tree[num1])
    tree_set2 = set(tree[num2])
    print(tree_set1)

    if tree_set1 <= tree_set2:
        result = tree_set1.union(tree_set2)
        break
    else:
