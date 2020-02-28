N = int(input())
max_result = 0
a = []
for i in range(int(N/2),N+1):
    n1 = N
    n2 = i
    result = [n1, n2]
    n3 = 0
    while n3 >= 0:
        n3 = n1-n2
        result.append(n3)
        n1 = n2
        n2 = n3
    if len(result) > max_result:
        max_result = len(result)
        a = result
print(max_result-1)
print(' '.join(map(str, a[0:max_result-1])))