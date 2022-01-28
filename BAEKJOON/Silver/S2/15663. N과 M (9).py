import sys
input = sys.stdin.readline


def subsequence(k):
    if k == M and tuple(result) not in overlap:
        print(*result)
        overlap.add(tuple(result))
    else:
        for i in range(N):
            if chk[i] == False:
                chk[i] = True
                result.append(array[i])
                subsequence(k+1)
                result.pop()
                chk[i] = False


N, M = map(int, input().split())
array = sorted(list(map(int, input().split())))
chk = [False for _ in range(N)]
overlap = set()
result = []
subsequence(0)
