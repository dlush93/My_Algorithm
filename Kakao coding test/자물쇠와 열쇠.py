key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate(key):
    result = [[0]*M for i in range(M)]
    for i in range(M):
        for j in range(M):
            result[j][M-1-i] = key[i][j]
    return result


M = len(key)
N = len(lock)
hole = []
for i in range(N):
    for j in range(N):
        if lock[i][j] == 0:
            hole.append([i,2-j])
            print(hole)
print(rotate(key))