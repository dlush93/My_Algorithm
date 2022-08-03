def next_permutation(num):
    for i in range(len(num)-1, 0, -1):
        if num[i] > num[i-1]:
            index = i-1
            break
    else:
        return num

    for j in range(len(num)-1, index, -1):
        if num[j] > num[index]:
            num[j], num[index] = num[index], num[j]
            break
    num = num[:index+1] + list(reversed(num[index+1:]))
    return num


for t in range(int(input())):
    word = input()
    num = list(map(ord, word))
    num = list(map(chr, next_permutation(num)))
    print(''.join(num))