N = int(input())
array = [[] for i in range(50)]
for i in range(N):
    word = input()
    array[len(word)-1].append(word)
for arr in array:
    data = sorted(set(arr))
    for d in data:
        print(d)
