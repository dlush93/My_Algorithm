for t in range(1, int(input())+1):
    A, B = map(int, input().split())
    count = 0
    for num in range(A, B+1):
        if num**(1/2) == int(num**(1/2)):
            if str(num) == str(num)[::-1]:
                if str(int(num**(1/2))) == str(int(num**(1/2)))[::-1]:
                    count += 1
                    
    print('#{} {}'.format(t, count))