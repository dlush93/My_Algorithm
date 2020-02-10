for t in range(1, int(input())+1):
    Ni, Nj = map(int, input().split())
    data = [input() for x in range(Ni)]
    for i in range(int(Ni/2)):
        for j in range(int(Nj/2)):
