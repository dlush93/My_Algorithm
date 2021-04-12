string = input()
board = []
temp = ''
for i in range(len(string)):
    if string[i] == 'X':
        temp += 'X'
    else:
        if len(temp) != 0:
            board.append(temp)
            temp = ''
            board.append('.')
        else:
            board.append('.')
if len(temp) !=0:
    board.append(temp)
result = ''
for b in board:
    if b == '.':
        result += '.'
    else:
        if len(b)%2:
            result = '-1'
            break
        else:
            if len(b)%4 == 0:
                result += 'AAAA'*(len(b)//4)
            else:
                result += 'AAAA'*(len(b)//4) + 'BB'
print(result)