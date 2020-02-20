def operator(a, num1, num2):
    if a == '+':
        return num2 + num1
    elif a == '-':
        return num2 - num1
    elif a == '*':
        return num2 * num1
    else:
        return num2 // num1


for t in range(1, int(input())+1):
    data = list(input().split())
    stack = []
    for i in data:
        if i.isdecimal():
            stack.append(int(i))
        elif i == '.':
            if len(stack) ==1:
                print('#{} {}'.format(t, stack.pop()))
            else:
                print('#{} error'.format(t))
        else:
            if len(stack) < 2:
                print('#{} error'.format(t))
                break
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operator(i, num1, num2))