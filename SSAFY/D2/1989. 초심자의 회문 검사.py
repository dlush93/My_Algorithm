for t in range(1, int(input())+1):
    word = input()
    if word == word[::-1]:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))