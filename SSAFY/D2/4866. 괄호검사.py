for t in range(1, int(input())+1):
    data = list(input())
    stack = []
    for i in data:
        if i == '{' or i == '(':
            stack.append(i)
            continue
        elif len(stack) !=0 and i == '}':
            a = stack.pop()
            if ord(i) != ord(a) +2:
                print('#{} 0'.format(t))
                break
        elif len(stack) !=0 and i == ')':
            a = stack.pop()
            if ord(i) != ord(a) +1:
                print('#{} 0'.format(t))
                break
        elif (i == '}' or i == ')') and len(stack) ==0:
            print('#{} 0'.format(t))
            break
    else:
        if len(stack) !=0:
            print('#{} 0'.format(t))
        else:
            print('#{} 1'.format(t))