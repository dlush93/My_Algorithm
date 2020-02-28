alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr = [-1]*26
data = input()
for i in range(len(data)):
    for j in range(len(alpha)):
        if arr[j] == -1 and data[i] == alpha[j]:
            arr[j] = i
print(*map(str, arr))