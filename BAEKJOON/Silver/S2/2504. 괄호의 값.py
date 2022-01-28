data = input()
open = []
operation = []
value = 1
temp = 0
for i in data:
    if i in ('(', '['):
        open.append(i)
    elif i == ')':
        if open[-1] == '[':
            print(0)
            break
        elif len(operation):
            
