for t in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    a = len(str1)
    b = len(str2)
    i = 0
    j = 0
    while i < a and j <b :
        if str1[i] != str2[j]:
            j = j-i
            i = -1
        i +=1
        j +=1
    if i == a:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))