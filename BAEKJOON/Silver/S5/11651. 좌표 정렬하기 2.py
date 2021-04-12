import sys
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
data_sort = sorted(data, key=lambda x: (x[1], x[0]))
for d in data_sort:
    print(' '.join(map(str, d)))