def binary_convert(num):
    a = len(num)
    b = 0
    for i in range(a):
        b += int(num[i])*2**(a-i-1)
    return b

def tenary_convert(num):
    a = len(num)
    b = 0
    for i in range(a):
        b += int(num[i])*3**(a-i-1)
    return b

for t in range(1, int(input())+1):
    binary = input()
    tenary = input()
    for i in range(len(binary)):
        if binary[i] == '1':
            num1 = binary_convert(binary) - 2**(len(binary)-1-i)
        else:
            num1 = binary_convert(binary) + 2**(len(binary)-1-i)
        for j in range(len(tenary)):
            if tenary[j] == '2':
                for k in range(1,3):
                    num2 = tenary_convert(tenary) - k*3**(len(tenary)-1-j)
                    if num1 == num2:
                        break
            elif tenary[j] == '1':
                for k in range(2):
                    num2 = tenary_convert(tenary) + ((-1)**k)*3**(len(tenary)-1-j)
                    if num1 == num2:
                        break
            else:
                for k in range(1,3):
                    num2 = tenary_convert(tenary) + k*3**(len(tenary)-1-j)
                    if num1 == num2:
                        break
            if num1 == num2:
                break
        if num1 == num2:
            break
    print('#{} {}'.format(t, num1))