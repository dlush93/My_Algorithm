from math import gcd

num = list(map(int, input().split()))
min_multiple = 1000000
for i in range(3):
    for j in range(i+1, 4):
        temp = num[i]*num[j]//gcd(num[i], num[j])
        for k in range(j+1, 5):
            multiple = temp*num[k]//gcd(temp, num[k])
            min_multiple = min(min_multiple, multiple)
print(min_multiple)