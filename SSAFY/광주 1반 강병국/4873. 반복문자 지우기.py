for t in range(1, int(input())+1):
    word = list(input())
    stack = []
    while len(word) !=0:
        if len(stack) ==0:
            stack.append(word.pop())
        elif stack[-1] == word[-1]:
            stack.pop()
            word.pop()
        else:
            stack.append(word.pop())
    print('#{} {}'.format(t, len(stack)))