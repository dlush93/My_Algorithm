import sys
input = sys.stdin.readline

N = int(input())
score = []
for i in range(N):
    name, kor, eng, math = input().split()
    score.append((name, int(kor), int(eng), int(math)))
score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(score[i][0])