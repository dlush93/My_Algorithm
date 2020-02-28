data = [int(input()) for i in range(10)]
stack = []
for t in data:
    num = t%42
    if num not in stack:
        stack.append(num)
print(len(stack))