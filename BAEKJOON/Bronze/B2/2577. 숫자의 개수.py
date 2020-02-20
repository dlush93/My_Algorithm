A = int(input())
B = int(input())
C = int(input())
ans = str(A*B*C)
arr = [0]*10
for i in ans:
    arr[int(i)] +=1
for i in range(10):
    print(arr[i])