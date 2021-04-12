import sys
N = int(sys.stdin.readline())
data = [list(sys.stdin.readline().split()) for i in range(N)]
data_sort = sorted(data, key=lambda x: int(x[0]))
for d in data_sort:
    print(' '.join(d))
