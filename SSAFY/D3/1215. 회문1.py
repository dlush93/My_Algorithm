for t in range(1,11):
    N = int(input())
    data = [list(input()) for x in range(8)]
    cnt = 0
    if N == 1:
        print('#{} 64'.format(t))
    else:
        for i in range(8):
            for j in range(8):
                ni = 0
                nj = 0
                while j + N < 9 and nj != N:
                    if data[i][j+nj] == data[i][j+N-1-nj]:
                        nj +=1
                    else:
                        break
                while i + N < 9 and ni != N:
                    if data[i+ni][j] == data[i+N-1-ni][j]:
                        ni +=1
                    else:
                        break
                if ni == N:
                    cnt +=1
                if nj == N:
                    cnt +=1
        print('#{} {}'.format(t, cnt))