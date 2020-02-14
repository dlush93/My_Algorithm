N = int(input())
result = ''
for i in range(1,N+1):
    n = 0
    for j in range(len(str(i))):
        if '3' in str(i)[j] or '6'in str(i)[j] or '9' in str(i)[j]:
            n +=1
    if n ==0:
        result += str(i) + ' '
    else:
        result += '-'*n +' '
print(result.rstrip())