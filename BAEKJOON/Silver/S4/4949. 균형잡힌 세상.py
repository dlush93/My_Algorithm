Flag = True
while Flag:
    sentence = input()
    open = []
    if sentence == '.':
        Flag = False
    else:
        for word in sentence:
            if word in ('[', '('):
                open.append(word)
            elif word == ']':
                if len(open) == 0:
                    print('no')
                    break
                elif open[-1] == '(':
                    print('no')
                    break
                else:
                    open.pop()
            elif word == ')':
                if len(open) == 0:
                    print('no')
                    break
                elif open[-1] == '[':
                    print('no')
                    break
                else:
                    open.pop()
        else:
            if len(open) != 0:
                print('no')
            else:
                print('yes')