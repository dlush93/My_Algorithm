test = int(input())
for t in range(1, test+1):
    A = input()
    a = len(A)
    arr0 = arr4 = '..#' + '...#'*(a-1)+'..'
    arr1 = arr3 = '.' + '#.#.'*(a)
    arr2 = '#'
    for i in range(a):
        arr2 = arr2 + '.'+ A[i] + '.#'
    print(arr0)
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)