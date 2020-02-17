def my_sqrt(num):
    b = num
    while b**2 > num:
        b -=1
    a = b+1
    for i in range(20):
        if ((a+b)/2)**2 > num:
            a = (a+b)/2
        else:
            b = (a+b)/2
    return a
print(my_sqrt(3))