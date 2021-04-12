N = input()
length = len(N)
result = []
end = 0
if int(N)-9*length < 0:
    end = 0
else:
    end = int(N)-9*length
for i in range(int(N), end, -1):
    temp = str(i)
    value = 0
    for j in range(len(temp)):
        value += int(temp[j])
    if i + value == int(N):
        result.append(i)
if len(result) != 0:
    print(result[-1])
else:
    print(0)