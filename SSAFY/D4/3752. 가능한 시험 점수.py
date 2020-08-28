for t in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    arr = [0] + data
    length = len(arr)
    result = []
    for d in data:
        for a in range(length):
            if d != arr[a] and d + arr[a] not in arr:
                arr.append(d+arr[a])
    print(arr)
