word =  [0]*2 + list(input())
cnt = len(word) - 2
for i in range(len(word)):
    if word[i] == 0:
        continue
    if word[i] == 'j':
        if word [i-1] == 'l' or word[i-1] == 'n':
            cnt -= 1
    elif word[i] == '-':
        if word[i-1] == 'c' or word[i-1] == 'd':
            cnt -= 1
    elif word[i] == '=':
        if word[i-1] == 'z':
            if word[i-2] == 'd':
                cnt -= 2
            else:
                cnt -= 1
        elif word[i-1] == 'c' or word[i-1] == 's':
            cnt -= 1
print(cnt)