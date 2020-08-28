N = int(input())
data = [list(input()) for i in range(N)]
length = len(data[0])
stack = data[0]
for i in data:
    for j in range(length):
        if stack[j] != i[j]:
            stack[j] = '?'
print(''.join(stack))