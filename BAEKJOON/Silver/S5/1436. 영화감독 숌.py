N = int(input())
arr = []
num = 666
while len(arr) != N:
    name = str(num)
    for i in range(len(name)-2):
        if name[i:i+3] == '666':
            arr.append(name)
            break
    num += 1
print(arr[N-1])