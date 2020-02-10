for t in range(1, int(input())+1):
    n, dir = input().split()
    N = int(n)
    data = [list(map(int, input().split())) for i in range(N)]
    arr = [[0]*N for i in range(N)]
    