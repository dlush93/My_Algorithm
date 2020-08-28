length, start = map(int, input().split())
data = list(map(int, input().split()))
arr = [[0]*100 for i in range(100)]
stack = []
for i in range(0, length, 2):
    arr[data[i]][data[i+1]] =1
