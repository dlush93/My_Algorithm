for t in range(1, int(input())+1):
    word = input()
    a = len(word)
    pal = True
    for i in range(a//2):
        if word[i] == word[a-i-1] or word[i] == '?' or word[a-i-1] == '?':
            pass
        else:
            print('#{} Not Exist'.format(t))
            pal = False
            break
    if pal == True:
        print('#{} Exist'.format(t))