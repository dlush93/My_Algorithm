for t in range(int(input())):
    k = int(input())
    n = int(input())
    array = [list(range(1, n+1))]
    for i in range(1, k+1):
        array.append([])
        for j in range(n):
            array[i].append(sum(array[i-1][:j+1]))
    print(array[k][n-1])