N, L = map(int, input().split())
fruits = sorted(list(map(int, input().split())))
for f in fruits:
    if f <= L:
        L += 1
print(L)