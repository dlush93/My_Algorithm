data = input()
time = 0
num = ['0', '0', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in data:
    for sec, j in enumerate(num,1):
        if i in j:
            time += sec
            break
print(time)