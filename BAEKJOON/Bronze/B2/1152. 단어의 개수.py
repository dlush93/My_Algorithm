data = input()
data = ' ' + data + ' '
n = 0
stack = []
for i in data:
    if i.isalpha():
        stack.append(i)
    else:
        if len(stack) !=0:
            n +=1
            stack = []
if len(stack) !=0:
    n +=1
print(n)