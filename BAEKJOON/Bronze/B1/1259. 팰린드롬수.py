t = 1
while t:
    num = input()
    if num != '0':
        if num == num[::-1]:
            print('yes')
        else:
            print('no')
    else:
        t = 0