for i in range(1, int(input()+1)):
    A, B = map(int, input().split())
    for num in range(A, B+1):
        if A <= num**2 <=