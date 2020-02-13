for t in range(1, int(input())+1):
    print('#{}'.format(t))
    N = int(input())
    data = [input().split() for i in range(N)]
    word = ''
    for i in range(N):
        word += data[i][0]*int(data[i][1])
    a = 0
    result = ''
    while a != len(word):
        if a%10 ==0:
