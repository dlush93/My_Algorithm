N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
weight = rope[0]
for i in range(1, N):
    if rope[i]*(i+1) > weight:
        weight = rope[i]*(i+1)
    else:
        break
print(weight)