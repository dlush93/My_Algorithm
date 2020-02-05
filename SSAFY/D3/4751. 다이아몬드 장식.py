test = int(input())
for t in range(1, test+1):
    char = input()
    a = len(char)
    arr = [['.']*((a-1)*4+5)for i in range(5)]
    arr[2][0] = '#'
    for j in range(5):
        for k in range((a-1)*4+5):
            if j == 0 or j == 4:
                for l in range(a):
                    if k == 4*l+2:
                        arr[j][k] = '#'
            elif j == 1 or j == 3:
                if k%2:
                    arr[j][k] = '#'
            else:
                for l in range(a):
                    if k == 4*l+4:
                        arr[j][k] = '#'
                    elif k == 4*l+2:
                        arr[j][k] = char[l]
    for q in range(5):
        print(''.join(arr[q]))

# test = int(input())
# for t in range(1, test+1):
#     A = input()
#     a = len(A)
#     arr0 = arr4 = '..#' + '...#'*(a-1)+'..'
#     arr1 = arr3 = '.' + '#.#.'*(a)
#     arr2 = '#'
#     for i in range(a):
#         arr2 = arr2 + '.'+ A[i] + '.#'
#     print(arr0)
#     print(arr1)
#     print(arr2)
#     print(arr3)
#     print(arr4)